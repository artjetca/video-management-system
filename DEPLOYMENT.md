# 视频管理系统部署指南

## 🚀 部署选项

### 选项 1: Heroku 部署（推荐用于 Flask 应用）

#### 1. 准备 Heroku 部署文件

创建 `Procfile`：
```
web: python app.py
```

创建 `requirements.txt`（已存在）

#### 2. 部署到 Heroku
```bash
# 安装 Heroku CLI
brew install heroku/brew/heroku

# 登录 Heroku
heroku login

# 创建应用
heroku create video-management-system-app

# 设置环境变量
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-very-secure-secret-key

# 部署
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

### 选项 2: Railway 部署

1. 访问 [Railway.app](https://railway.app)
2. 连接 GitHub 仓库
3. 选择 Python 模板
4. 设置环境变量：
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secure-key`
5. 部署完成

### 选项 3: Vercel 部署

创建 `vercel.json`：
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

部署命令：
```bash
npm i -g vercel
vercel --prod
```

### 选项 4: Netlify 静态部署

当前项目已配置为 Netlify 静态部署：

```bash
# 使用 Netlify CLI
netlify login
netlify init
netlify deploy --prod
```

## 🔧 生产环境配置

### 环境变量
- `FLASK_ENV=production`
- `SECRET_KEY=your-very-secure-secret-key`

### 数据库
- 生产环境建议使用 PostgreSQL
- 可以使用 Heroku Postgres 或 Railway PostgreSQL

### 文件上传
- 生产环境建议使用云存储（AWS S3, Google Cloud Storage）
- 当前配置支持本地文件上传

## 📝 部署后设置

1. 访问部署的 URL
2. 使用管理员凭据登录：
   - 用户名: `admin` 或 `admin@example.com`
   - 密码: `admin123`
3. 开始管理您的视频内容

## 🔒 安全建议

1. 更改默认管理员密码
2. 设置强密码策略
3. 启用 HTTPS（大多数平台自动提供）
4. 定期备份数据库

## 📞 支持

如需帮助，请查看各平台的官方文档：
- [Heroku Python 部署](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Railway 部署指南](https://docs.railway.app/deploy/deployments)
- [Vercel Python 部署](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
