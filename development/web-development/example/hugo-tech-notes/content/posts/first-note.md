---
title: "第一篇技术笔记"
date: 2026-09-20T09:00:00+08:00
description: "认识 Hugo 内容文件与 Front Matter。"
tags: [Hugo, Web]
draft: false
---

Hugo 会读取 Markdown 文件开头的 Front Matter，得到标题、日期、摘要和标签，再将正文交给模板渲染。

## 内容与样式分离

正文放在 `content/`，页面结构放在 `layouts/`，样式放在 `static/css/`。这种分工让作者可以专注写作，也让网站外观能够统一维护。

## 下一步

修改本文件并保存。运行 `hugo server -D` 时，浏览器会自动刷新并显示新内容。
