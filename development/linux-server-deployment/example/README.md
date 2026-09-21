# 服务器示例说明

本目录只提供配置样例，不是已经部署成功的服务器记录。

## 目标结构

```text
/srv/tech-notes/
└─ current/
   ├─ index.html
   ├─ posts/
   ├─ css/
   └─ js/

/etc/nginx/
├─ sites-available/
│  └─ DOMAIN
└─ sites-enabled/
   └─ DOMAIN -> ../sites-available/DOMAIN
```

把 `nginx-site.conf` 复制为 `/etc/nginx/sites-available/DOMAIN` 前，必须替换其中的 `DOMAIN` 和 `SITE_ROOT`。应用配置前运行：

```bash
# 运行环境：Ubuntu Bash；只检查配置，不重载服务
sudo nginx -t
```

只有看到语法与测试成功后，才执行 `sudo systemctl reload nginx`。HTTPS 配置由 Certbot 在域名解析生效、80/443 端口可访问后生成，不能把本目录的 HTTP 配置当成最终 TLS 配置。
