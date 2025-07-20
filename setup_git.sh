#!/bin/bash

# 视频管理系统 Git 设置脚本

echo "🚀 初始化 Git 仓库..."

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 创建初始提交
git commit -m "Initial commit: Video Management System

Features:
- Flask web application
- User authentication
- Video management (CRUD)
- Google Drive integration
- Bootstrap UI
- SQLite database
- Multiple deployment options

Deployment ready for:
- Heroku
- Railway
- Vercel
- Netlify (static)"

echo "✅ Git 仓库初始化完成！"
echo ""
echo "📋 下一步："
echo "1. 在 GitHub 上创建新仓库"
echo "2. 运行以下命令连接远程仓库："
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "🚀 然后选择部署平台："
echo "- Railway: https://railway.app (推荐)"
echo "- Heroku: heroku create your-app-name"
echo "- Vercel: vercel --prod"
echo ""
echo "📖 详细部署指南请查看 COMPLETE_DEPLOYMENT.md"
