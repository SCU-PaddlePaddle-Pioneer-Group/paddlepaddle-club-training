# 飞桨社团技术培训资料库

面向四川大学飞桨领航团成员的技术培训与自学资料库，沉淀社团技术分享、课程讲义、实践代码、项目复盘和学习路线。

资料按两个方向组织：

- **开发**：编程基础、Git 与团队协作、Web 开发、数据库、测试、DevOps 与软件架构。
- **AI**：数学与编程基础、机器学习、深度学习、生成式 AI、LLM 应用与 AI 工程。

> 当前仓库已正式收录 2 份教程：1 份开发类教程和 1 份 AI 类教程。后续新增教程时，会同步更新教程导航、内容索引、更新记录、制作参与者和贡献者名录。

## 当前资料状态

| 方向 | 当前状态 | 已收录内容 |
| --- | --- | --- |
| 开发 | 已有正式教程 | 团队开发与 Git 操作指南 v1.0.0 |
| AI | 已有正式教程 | CNN 从原理到实践（首次收录） |

## 教程导航

| 期次 / 主题 | 方向 | 主要教程内容 | 状态 | 资料入口 |
| --- | --- | --- | --- | --- |
| 教程 01：团队开发与 Git 操作 | 开发 | Git 基础、GitHub 协作、Windows 环境准备、功能分支、Pull Request、Fork、main-only 流程、代码评审、冲突处理、安全撤销与故障排查 | 已发布 v1.0.0 | [阅读教程](./development/git-and-collaboration/团队开发与Git操作指南.md) |
| 教程 02：CNN 从原理到实践 | AI | 图像张量、卷积计算、多通道卷积、输出尺寸、参数量、激活函数、归一化、池化、感受野、分类损失、训练过程、经典 CNN 架构和 CIFAR-10 实践 | 已收录 | [阅读教程](./ai/cnn-from-principles-to-practice/CNN%20从原理到实践.md) |

新增教程后，请在上表登记期次、方向、主要内容、版本和资料入口；未发布的培训想法暂不列入“已发布教程”。

## 已收录教程内容

### 教程 01：团队开发与 Git 操作

本教程适合首次参与团队开发、尚未系统使用 Git 与 GitHub 的成员，主要内容包括：

1. 团队开发与版本控制的基本概念、角色和安全操作顺序。
2. Git 与 GitHub 的职责边界、仓库对象、权限和可见性。
3. Windows 环境下 Git、VS Code、身份认证和首次克隆配置。
4. `status`、`diff`、`add`、`commit`、分支、远程仓库和合并等基础操作。
5. 功能分支、Pull Request、代码评审、合并和分支清理。
6. Fork 协作、`origin` / `upstream` 双远程和跨仓库 Pull Request。
7. `main-only` 分支与交付流程、阶段边界、Hotfix、Tag 和回滚。
8. Pull Request 描述、Review 结果、作者自检和评审者检查清单。
9. 冲突处理、Merge Editor、`revert` 与不同状态下的安全撤销。
10. 常见故障排查、操作检查清单、高频命令和 Git 术语表。

教程正文和配图位于 [`development/git-and-collaboration/`](./development/git-and-collaboration/)。

### 教程 02：CNN 从原理到实践

本教程从一次卷积计算出发，结合图解、公式和可运行代码，逐步介绍 CNN 的结构、原理和训练过程，主要内容包括：

1. CNN 相比全连接网络在图像任务中的局部连接、参数共享和分层表示。
2. 图像张量的 NCHW / NHWC 排列、归一化和训练数据增强。
3. 单通道与多通道卷积、互相关、分组卷积、输出尺寸、参数量和计算量。
4. ReLU、Leaky ReLU 等激活函数，以及 BatchNorm、GroupNorm 和 LayerNorm。
5. 最大池化、平均池化、带步幅卷积和全局平均池化。
6. 理论感受野、有效感受野以及多层小卷积核的作用。
7. logits、Softmax、交叉熵和 PyTorch `CrossEntropyLoss` 的正确使用方式。
8. 反向传播、优化器、正则化、验证集和过拟合排查。
9. LeNet-5、AlexNet、VGG、ResNet 到现代视觉架构的演进。
10. 使用 PyTorch 在 CIFAR-10 上训练和评估一个小型 CNN，并保存验证集最优权重。

教程正文、训练脚本和配图位于 [`ai/cnn-from-principles-to-practice/`](./ai/cnn-from-principles-to-practice/)。

## 教程更新记录

这里记录教程内容和资料库的重要更新；仓库自动生成的提交记录可在 GitHub 的 Commits 页面查看。

| 日期 | 教程 / 文件 | 版本 | 更新内容 | 参与者 |
| --- | --- | --- | --- | --- |
| 2026-09-04 | CNN 从原理到实践 | 首次收录 | 收录 CNN 原理教程、CIFAR-10 PyTorch 训练脚本和 PNG/SVG 配图 | Jack Yao / @Vantalens |
| 2026-09-14 | 团队开发与 Git 操作指南 | v1.0.0 | 首次发布，覆盖 Git 与 GitHub 基础、功能分支、Fork、Pull Request、评审、冲突、安全撤销和故障排查 | Jack Yao |
| 2026-09-21 | CNN 从原理到实践 | v1.0.1 | 补充作者署名：Jack Yao / @Vantalens | Jack Yao |
| 2026-09-21 | AI 分类说明与仓库 README | v1.2.0 | 加入 CNN 教程导航、AI 分类入口、主要内容索引和当前资料状态 | Jack Yao |

后续更新教程时，建议记录变更日期、版本号、主要改动、影响章节、验证方式和参与者。

## 教程制作参与者名录

以下名单依据当前源文件和仓库提交记录整理。CNN 教程作者为 Jack Yao / @Vantalens；如有其他制作参与者，后续将在确认本人信息后补充。

| 姓名 / GitHub 账号 | 参与角色 | 已确认工作 | 参与教程 |
| --- | --- | --- | --- |
| Jack Yao / [@Vantalens](https://github.com/Vantalens) | 教程编写与迭代 | 编写并维护《团队开发与 Git 操作指南》源文件 | 教程 01 |
| Jack Yao / [@Vantalens](https://github.com/Vantalens) | 原始作者、编写与维护 | 编写并维护《CNN 从原理到实践》 | 教程 02 |
| Jack Yao / [@Vantalens](https://github.com/Vantalens) | 资料整理与仓库维护 | 创建资料仓库、上传两份教程及配图/代码、维护目录和 README | 教程 01、教程 02、仓库整体 |

## 贡献者名录

截至当前版本，仓库中已确认的贡献者如下：

| 贡献者 | 贡献类型 | 已完成内容 |
| --- | --- | --- |
| Jack Yao / [@Vantalens](https://github.com/Vantalens) | 文档、代码、资料整理、仓库维护 | 初始化仓库，收录 Git 教程和 CNN 教程，上传配图与 CIFAR-10 训练脚本，维护分类说明和 README；CNN 教程作者为 Jack Yao |

也可以查看 GitHub 自动生成的[贡献者列表](https://github.com/SCU-PaddlePaddle-Pioneer-Group/paddlepaddle-club-training/graphs/contributors)。后续新增贡献者时，请记录真实发生且可追溯的文档、代码、勘误、测试反馈或培训建议，并在本人同意后公开姓名或账号。

## 特别鸣谢

特别感谢：

- [四川大学飞桨领航团](https://github.com/SCU-PaddlePaddle-Pioneer-Group)，提供学习、实践和开源协作的平台。
- [PaddlePaddle / 飞桨](https://www.paddlepaddle.org.cn/)，为社团 AI 学习与实践提供开源工具和生态支持。
- Git 教程参考的 [Git 官方文档](https://git-scm.com/docs)、[Pro Git 中文版](https://git-scm.com/book/zh/v2)、[GitHub 官方文档](https://docs.github.com/zh/get-started) 和 [Visual Studio Code 文档](https://code.visualstudio.com/docs/sourcecontrol/overview)。
- CNN 教程参考的论文、知乎文章以及 [PyTorch `Conv2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)、[`BatchNorm2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html) 和 [`CrossEntropyLoss`](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) 官方文档。
- 后续参与授课、讨论、试用、反馈和资料整理的每一位社团成员。

如有遗漏或希望调整公开信息，请通过 Issue 或 Pull Request 联系维护者。

## 资料组织约定

每个培训主题建议单独建立目录，并包含：

```text
topic-name/
├── README.md      # 学习目标、先修知识与课程大纲
├── notes/         # 讲义与知识点
├── examples/      # 示例代码或练习
└── exercises/     # 作业、实践题与参考答案
```

## 社团协作

1. 在 `development/` 或 `ai/` 下创建主题目录。
2. 为主题补充学习目标、资料来源、实践任务和适用人群。
3. 示例代码应注明运行环境；外部资料请保留原始链接与许可证信息。
4. 提交 Pull Request，并在描述中说明教程期次、培训时长、分享人和验证结果。
5. 更新教程时同步维护教程导航、更新记录、参与者名录和贡献者名录。

## 许可证

本仓库中的原创资料默认采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)；第三方资料遵循其原始许可证。