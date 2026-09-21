# 飞桨社团技术培训资料库

面向四川大学飞桨领航团成员的技术培训与自学资料库，沉淀社团技术分享、课程讲义、实践代码、项目复盘和学习路线。

资料按两个方向组织：

- **开发**：编程基础、Git 与团队协作、Web 开发、数据库、测试、DevOps 与软件架构。
- **AI**：数学与编程基础、机器学习、深度学习、生成式 AI、LLM 应用与 AI 工程。

> 当前仓库已正式收录 1 份开发类教程。后续新增教程时，会同步更新教程导航、更新记录、制作参与者和贡献者名录。

## 当前资料状态

| 方向 | 当前状态 | 已收录内容 |
| --- | --- | --- |
| 开发 | 已有正式教程 | 团队开发与 Git 操作指南 v1.0.0 |
| AI | 分类目录已建立，暂无正式教程 | 暂无 |

## 教程导航

| 期次 / 主题 | 方向 | 主要教程内容 | 状态 | 资料入口 |
| --- | --- | --- | --- | --- |
| 教程 01：团队开发与 Git 操作 | 开发 | Git 基础、GitHub 协作、Windows 环境准备、功能分支、Pull Request、Fork、main-only 流程、代码评审、冲突处理、安全撤销与故障排查 | 已发布 v1.0.0 | [阅读教程](./development/git-and-collaboration/团队开发与Git操作指南.md) |

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

## 教程更新记录

这里记录教程内容和资料库的重要更新；仓库自动生成的提交记录可在 GitHub 的 Commits 页面查看。

| 日期 | 教程 / 文件 | 版本 | 更新内容 | 参与者 |
| --- | --- | --- | --- | --- |
| 2026-09-14 | 团队开发与 Git 操作指南 | v1.0.0 | 首次发布，覆盖 Git 与 GitHub 基础、功能分支、Fork、Pull Request、评审、冲突、安全撤销和故障排查 | Jack Yao |
| 2026-09-21 | 培训资料库 README | v1.1.0 | 根据当前收录情况补充资料状态、教程导航、内容索引、参与者、贡献者和鸣谢信息 | Jack Yao |

后续更新教程时，建议记录变更日期、版本号、主要改动、影响章节、验证方式和参与者。

## 教程制作参与者名录

以下名单依据当前源文件和仓库提交记录整理。后续如有授课、审阅、实验验证、配图制作或内容补充人员，将在确认本人信息后补充。

| 姓名 / GitHub 账号 | 参与角色 | 已确认工作 | 参与教程 |
| --- | --- | --- | --- |
| Jack Yao / [@Vantalens](https://github.com/Vantalens) | 教程编写与迭代 | 编写并维护《团队开发与 Git 操作指南》源文件 | 教程 01 |
| Jack Yao / [@Vantalens](https://github.com/Vantalens) | 资料整理与仓库维护 | 创建资料仓库、上传教程正文与配图、维护目录和 README | 仓库整体 |

## 贡献者名录

截至当前版本，仓库中已确认的贡献者如下：

| 贡献者 | 贡献类型 | 已完成内容 |
| --- | --- | --- |
| Jack Yao / [@Vantalens](https://github.com/Vantalens) | 文档、资料整理、仓库维护 | 初始化仓库，收录 Git 教程及配图，维护分类说明和 README |

也可以查看 GitHub 自动生成的[贡献者列表](https://github.com/SCU-PaddlePaddle-Pioneer-Group/paddlepaddle-club-training/graphs/contributors)。后续新增贡献者时，请记录真实发生且可追溯的文档、代码、勘误、测试反馈或培训建议，并在本人同意后公开姓名或账号。

## 特别鸣谢

特别感谢：

- [四川大学飞桨领航团](https://github.com/SCU-PaddlePaddle-Pioneer-Group)，提供学习、实践和开源协作的平台。
- [PaddlePaddle / 飞桨](https://www.paddlepaddle.org.cn/)，为社团 AI 学习与实践提供开源工具和生态支持。
- [Git 官方文档](https://git-scm.com/docs)、[Pro Git 中文版](https://git-scm.com/book/zh/v2)、[GitHub 官方文档](https://docs.github.com/zh/get-started) 和 [Visual Studio Code 文档](https://code.visualstudio.com/docs/sourcecontrol/overview)，为 Git 教程提供参考资料。
- 后续参与授课、讨论、试用、反馈和资料整理的每一位社团成员。

如有遗漏或希望调整公开信息，请通过 Issue 或 Pull Request 联系维护者。

## 资料组织约定

每个培训主题建议单独建立目录，并包含：

```text
topic-name/
├── README.md       # 学习目标、先修知识与课程大纲
├── notes/          # 讲义与知识点
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