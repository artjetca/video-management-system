#!/bin/bash

# 🚀 快速部署脚本 - 西班牙语视频管理系统

echo "🎬 西班牙语视频管理系统 - 快速部署"
echo "=================================="

# 检查 Git 状态
echo "📋 检查 Git 状态..."
if [ ! -d ".git" ]; then
    echo "❌ 错误：未找到 Git 仓库"
    exit 1
fi

# 提交最新更改
echo "💾 提交最新更改..."
git add .
git status

# 显示部署选项
echo ""
echo "🚀 选择部署平台："
echo "1) Railway (推荐) - 最简单的部署方式"
echo "2) Heroku - 经典的云平台"
echo "3) Vercel - 现代化部署平台"
echo "4) 手动部署指南"
echo ""

read -p "请选择部署平台 (1-4): " choice

case $choice in
    1)
        echo "🚂 Railway 部署指南："
        echo ""
        echo "1. 首先推送到 GitHub："
        echo "   git remote add origin https://github.com/YOUR_USERNAME/video-management-system.git"
        echo "   git branch -M main"
        echo "   git push -u origin main"
        echo ""
        echo "2. 访问 https://railway.app"
        echo "3. 使用 GitHub 账户登录"
        echo "4. 点击 'New Project' -> 'Deploy from GitHub repo'"
        echo "5. 选择您的仓库"
        echo "6. 设置环境变量："
        echo "   FLASK_ENV=production"
        echo "   SECRET_KEY=your-secure-key-12345"
        echo ""
        echo "🎉 部署完成后，您将获得一个 .railway.app 域名！"
        ;;
    2)
        echo "🟣 Heroku 部署："
        echo ""
        echo "安装 Heroku CLI："
        echo "brew install heroku/brew/heroku"
        echo ""
        echo "部署命令："
        echo "heroku login"
        echo "heroku create your-video-app"
        echo "heroku config:set FLASK_ENV=production"
        echo "heroku config:set SECRET_KEY=your-secure-key"
        echo "git push heroku main"
        ;;
    3)
        echo "⚡ Vercel 部署："
        echo ""
        echo "安装 Vercel CLI："
        echo "npm i -g vercel"
        echo ""
        echo "部署命令："
        echo "vercel --prod"
        ;;
    4)
        echo "📖 打开详细部署指南..."
        if command -v open &> /dev/null; then
            open DEPLOY_GUIDE.md
        else
            echo "请查看 DEPLOY_GUIDE.md 文件获取详细指南"
        fi
        ;;
    *)
        echo "❌ 无效选择"
        exit 1
        ;;
esac

echo ""
echo "📋 系统信息："
echo "- 界面语言: 西班牙语"
echo "- 登录凭据: admin / admin123"
echo "- 功能: Google Drive 集成, 过期控制, 下载保护"
echo "- 示例数据: 已包含 3 个示例视频"
echo ""
echo "🎉 祝您部署成功！"
