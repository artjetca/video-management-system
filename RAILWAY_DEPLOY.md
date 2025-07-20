# 🚂 Railway 部署指南

由于 Netlify 主要支持静态网站，Flask 后端无法正常运行。我推荐使用 Railway 来部署完整的 Flask 应用。

## 🚀 Railway 部署步骤

### 1. 准备 GitHub 仓库

首先将项目推送到 GitHub：

```bash
# 在项目目录中执行
cd /Users/macbookpro/CascadeProjects/video-management-system

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 创建提交
git commit -m "Enhanced Video Management System with Google Drive integration"

# 在 GitHub 上创建新仓库，然后连接
git remote add origin https://github.com/YOUR_USERNAME/video-management-system.git
git branch -M main
git push -u origin main
```

### 2. 部署到 Railway

1. **访问 Railway**
   - 打开 https://railway.app
   - 使用 GitHub 账户登录

2. **创建新项目**
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择您的 video-management-system 仓库

3. **自动部署**
   - Railway 会自动检测到这是一个 Python 项目
   - 自动安装 requirements.txt 中的依赖
   - 自动运行 app.py

4. **设置环境变量**
   - 在 Railway 项目设置中添加：
   ```
   FLASK_ENV=production
   SECRET_KEY=your-very-secure-secret-key-here
   ```

5. **获取部署 URL**
   - Railway 会提供一个自动生成的 URL
   - 例如：https://your-app-name.railway.app

## 🔧 其他部署选项

### Heroku 部署
```bash
# 安装 Heroku CLI
brew install heroku/brew/heroku

# 登录 Heroku
heroku login

# 创建应用
heroku create your-video-app-name

# 设置环境变量
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secure-key

# 部署
git push heroku main
```

### Vercel 部署
```bash
# 安装 Vercel CLI
npm i -g vercel

# 部署
vercel --prod
```

## 📋 部署后验证

部署成功后，您应该能够：

1. **访问登录页面**
   - URL: https://your-app.railway.app/login
   - 用户名: admin 或 admin@example.com
   - 密码: admin123

2. **测试功能**
   - 添加 Google Drive 视频
   - 设置过期日期
   - 控制下载权限
   - 观看视频

## 🆘 故障排除

如果遇到问题：

1. **检查日志**
   - Railway: 在项目面板查看部署日志
   - Heroku: 使用 `heroku logs --tail`

2. **常见问题**
   - 端口配置：确保使用环境变量 PORT
   - 依赖安装：检查 requirements.txt
   - 数据库：SQLite 在某些平台可能需要特殊配置

3. **联系支持**
   - Railway: https://railway.app/help
   - Heroku: https://help.heroku.com

## 🎯 推荐方案

**最简单的部署方式：**

1. 推送代码到 GitHub
2. 访问 https://railway.app
3. 连接 GitHub 仓库
4. 一键部署！

部署完成后，您将获得一个完全功能的视频管理系统，支持所有增强功能！
