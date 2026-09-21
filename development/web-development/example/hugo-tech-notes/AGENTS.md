# 技术手记示例站协作说明

## 项目结构

- `content/`：Markdown 内容。
- `layouts/`：Hugo 页面模板。
- `static/`：原样复制到输出目录的 CSS 与 JavaScript。
- `hugo.toml`：站点配置；示例占位符不得替换成私人凭据。

## 验证命令

```powershell
hugo --minify --cleanDestinationDir
git diff --check
```

## 修改规则

- 保持纯 Hugo、HTML、CSS 和原生 JavaScript，不增加 Node.js 或前端框架。
- 保留语义化 HTML、键盘可访问性和 `prefers-reduced-motion` 支持。
- 新增内容使用相对或 Hugo 生成的链接，不硬编码本地绝对路径。
- 不提交 `public/`、密钥、令牌或真实服务器信息。
- 完成条件：构建成功，首页、列表页和详情页可生成，差异中没有无关改动。
