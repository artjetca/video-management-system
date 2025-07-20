# 🚀 部署指南 - 西班牙语视频管理系统

## 📋 部署前准备

您的系统已经准备好部署，包含：
- ✅ 完整的西班牙语界面
- ✅ Google Drive 视频集成
- ✅ 过期日期控制
- ✅ 下载保护功能
- ✅ 示例数据

## 🎯 推荐部署方案：Railway（最简单）

### 步骤 1：推送到 GitHub

```bash
# 在项目目录中执行
cd /Users/macbookpro/CascadeProjects/video-management-system

# 创建 GitHub 仓库后，连接远程仓库
git remote add origin https://github.com/YOUR_USERNAME/video-management-system.git
git branch -M main
git push -u origin main
```

### 步骤 2：部署到 Railway

1. **访问 Railway**
   - 打开 https://railway.app
   - 使用 GitHub 账户登录

2. **创建新项目**
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择您的 `video-management-system` 仓库

3. **自动部署**
   - Railway 会自动检测 Python 项目
   - 自动安装 requirements.txt 中的依赖
   - 自动运行应用

4. **设置环境变量**
   在 Railway 项目设置中添加：
   ```
   FLASK_ENV=production
   SECRET_KEY=your-very-secure-secret-key-here-12345
   PORT=8080
   ```

5. **获取部署 URL**
   - Railway 会提供一个 URL，例如：
   - `https://your-app-name.railway.app`

## 🔧 其他部署选项

### Option 2: Heroku

```bash
# 安装 Heroku CLI
brew install heroku/brew/heroku

# 登录 Heroku
heroku login

# 创建应用
heroku create your-video-app-name

# 设置环境变量
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secure-key-12345

# 部署
git push heroku main
```

### Option 3: Vercel

```bash
# 安装 Vercel CLI
npm i -g vercel

# 部署
vercel --prod
```

### Option 4: DigitalOcean App Platform

1. 连接 GitHub 仓库
2. 选择 Python 环境
3. 设置环境变量
4. 一键部署

## 📝 部署后配置

### 环境变量设置

无论选择哪个平台，都需要设置以下环境变量：

```bash
FLASK_ENV=production
SECRET_KEY=your-very-secure-secret-key-here-12345
PORT=8080  # 某些平台会自动设置
```

### 登录凭据

部署后，使用以下凭据登录：
- **用户名**: `admin` 或 `admin@example.com`
- **密码**: `admin123`

## 🎉 部署成功验证

部署成功后，您应该能够：

1. **访问登录页面**
   - 看到完整的西班牙语界面
   - "Sistema de Gestión de Videos"

2. **登录系统**
   - 使用 admin/admin123 登录
   - 进入 "Panel de Control"

3. **查看示例数据**
   - 3个示例视频
   - 不同的过期状态
   - 西班牙语标题和描述

4. **测试功能**
   - 添加新视频
   - 设置过期日期
   - 控制下载权限

## 🆘 故障排除

### 常见问题

1. **构建失败**
   - 检查 requirements.txt 是否正确
   - 确保 Python 版本兼容（3.8+）

2. **数据库错误**
   - 应用会自动创建 SQLite 数据库
   - 首次运行会自动初始化

3. **端口问题**
   - 确保设置了正确的 PORT 环境变量
   - 大多数平台会自动分配端口

4. **静态文件问题**
   - Bootstrap 和 Font Awesome 通过 CDN 加载
   - 无需额外配置

### 获取帮助

- **Railway**: https://railway.app/help
- **Heroku**: https://help.heroku.com
- **Vercel**: https://vercel.com/docs

## 🎯 生产环境建议

1. **更改默认密码**
   - 登录后立即更改管理员密码

2. **备份数据库**
   - 定期备份 SQLite 数据库文件

3. **监控日志**
   - 查看应用日志以监控性能

4. **SSL 证书**
   - 大多数平台会自动提供 HTTPS

## 📞 支持

如果遇到部署问题，请提供：
- 选择的部署平台
- 错误信息截图
- 部署日志

祝您部署成功！🎉
