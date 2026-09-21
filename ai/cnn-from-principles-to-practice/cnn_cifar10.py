"""A compact, reproducible CIFAR-10 CNN baseline used by the companion blog.

Run:
    python cnn_cifar10.py --epochs 20 --data-dir ./data

The script downloads CIFAR-10 when it is not already present.
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms


CIFAR10_MEAN = (0.4914, 0.4822, 0.4465)
CIFAR10_STD = (0.2470, 0.2435, 0.2616)


class SmallCNN(nn.Module):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 64, 3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 128, 3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
        )
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Linear(128, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.pool(x)
        x = torch.flatten(x, 1)
        return self.classifier(x)


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def make_loaders(
    data_dir: Path,
    batch_size: int,
    workers: int,
    seed: int,
    validation_size: int,
) -> tuple[DataLoader, DataLoader, DataLoader]:
    train_transform = transforms.Compose(
        [
            transforms.RandomCrop(32, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(CIFAR10_MEAN, CIFAR10_STD),
        ]
    )
    test_transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(CIFAR10_MEAN, CIFAR10_STD),
        ]
    )
    augmented_train_set = datasets.CIFAR10(
        data_dir, train=True, download=True, transform=train_transform
    )
    evaluation_train_set = datasets.CIFAR10(
        data_dir, train=True, download=False, transform=test_transform
    )
    test_set = datasets.CIFAR10(data_dir, train=False, download=True, transform=test_transform)
    if not 1 <= validation_size < len(augmented_train_set):
        raise ValueError("validation-size must be between 1 and the training-set size")
    generator = torch.Generator().manual_seed(seed)
    indices = torch.randperm(len(augmented_train_set), generator=generator).tolist()
    validation_indices = indices[:validation_size]
    training_indices = indices[validation_size:]
    train_set = Subset(augmented_train_set, training_indices)
    validation_set = Subset(evaluation_train_set, validation_indices)
    pin_memory = torch.cuda.is_available()
    train_loader = DataLoader(
        train_set,
        batch_size=batch_size,
        shuffle=True,
        num_workers=workers,
        pin_memory=pin_memory,
        persistent_workers=workers > 0,
    )
    test_loader = DataLoader(
        test_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=workers,
        pin_memory=pin_memory,
        persistent_workers=workers > 0,
    )
    validation_loader = DataLoader(
        validation_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=workers,
        pin_memory=pin_memory,
        persistent_workers=workers > 0,
    )
    return train_loader, validation_loader, test_loader


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> tuple[float, float]:
    model.train()
    loss_sum = 0.0
    correct = 0
    count = 0
    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)

        optimizer.zero_grad(set_to_none=True)
        logits = model(images)
        loss = loss_fn(logits, labels)
        loss.backward()
        optimizer.step()

        batch_size = labels.size(0)
        loss_sum += loss.item() * batch_size
        correct += (logits.argmax(dim=1) == labels).sum().item()
        count += batch_size
    return loss_sum / count, correct / count


@torch.inference_mode()
def evaluate(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    device: torch.device,
) -> tuple[float, float]:
    model.eval()
    loss_sum = 0.0
    correct = 0
    count = 0
    for images, labels in loader:
        images = images.to(device, non_blocking=True)
        labels = labels.to(device, non_blocking=True)
        logits = model(images)
        loss = loss_fn(logits, labels)
        batch_size = labels.size(0)
        loss_sum += loss.item() * batch_size
        correct += (logits.argmax(dim=1) == labels).sum().item()
        count += batch_size
    return loss_sum / count, correct / count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a small CNN on CIFAR-10")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--learning-rate", type=float, default=3e-3)
    parser.add_argument("--weight-decay", type=float, default=5e-4)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--validation-size", type=int, default=5_000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=Path, default=Path("small_cnn_best.pt"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.epochs < 1 or args.batch_size < 1 or args.workers < 0:
        raise ValueError("epochs and batch-size must be positive; workers cannot be negative")

    seed_everything(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_loader, validation_loader, test_loader = make_loaders(
        args.data_dir,
        args.batch_size,
        args.workers,
        args.seed,
        args.validation_size,
    )
    model = SmallCNN().to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.learning_rate, weight_decay=args.weight_decay
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    with torch.inference_mode():
        shape = model(torch.zeros(2, 3, 32, 32, device=device)).shape
    assert shape == (2, 10), f"Unexpected output shape: {shape}"

    best_accuracy = -1.0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    print(f"device={device}; parameters={sum(p.numel() for p in model.parameters()):,}")
    for epoch in range(1, args.epochs + 1):
        train_loss, train_accuracy = train_one_epoch(model, train_loader, loss_fn, optimizer, device)
        validation_loss, validation_accuracy = evaluate(
            model, validation_loader, loss_fn, device
        )
        scheduler.step()
        print(
            f"epoch={epoch:02d} "
            f"train_loss={train_loss:.4f} train_acc={train_accuracy:.2%} "
            f"val_loss={validation_loss:.4f} val_acc={validation_accuracy:.2%}"
        )
        if validation_accuracy > best_accuracy:
            best_accuracy = validation_accuracy
            torch.save(
                {
                    "model_state": model.state_dict(),
                    "validation_accuracy": validation_accuracy,
                    "epoch": epoch,
                    "classes": test_loader.dataset.classes,
                },
                args.output,
            )

    checkpoint = torch.load(args.output, map_location=device)
    model.load_state_dict(checkpoint["model_state"])
    test_loss, test_accuracy = evaluate(model, test_loader, loss_fn, device)
    print(
        f"best_val_acc={best_accuracy:.2%}; "
        f"test_loss={test_loss:.4f}; test_acc={test_accuracy:.2%}; "
        f"checkpoint={args.output}"
    )


if __name__ == "__main__":
    main()
