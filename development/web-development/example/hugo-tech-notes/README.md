# Hugo 技术手记示例

这是教程配套的最小完整 Hugo 网站，不使用主题、Node.js 或前端框架。

```powershell
# 运行环境：Windows PowerShell 7
hugo server -D
```

打开终端显示的本地地址。生成生产文件：

```powershell
hugo --minify --cleanDestinationDir
```

构建结果位于 `public/`。部署到 GitHub Pages 前，把 `hugo.toml` 中的 `GITHUB_USER` 和 `REPOSITORY` 替换为实际值，并在仓库设置中选择 Pages 的 GitHub Actions 发布源。
