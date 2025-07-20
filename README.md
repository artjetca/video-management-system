# 视频管理系统

一个基于 Flask 的现代化视频管理系统，支持视频上传、Google Drive 集成和管理员权限控制。

## 功能特性

### 🔐 用户认证
- 安全的登录系统
- 管理员权限控制
- 会话管理

### 📹 视频管理
- 添加新视频（本地上传或 Google Drive 链接）
- 编辑视频信息
- 归档/恢复视频
- 删除视频
- 视频搜索功能

### 🎨 现代化界面
- 响应式设计，支持移动端
- Bootstrap 5 美观界面
- Font Awesome 图标
- 渐变色彩设计

### 📊 仪表板
- 视频统计概览
- 最近添加的视频
- 快速操作面板

## 默认登录凭据

```
用户名: admin 或 admin@example.com
密码: admin123
```

## 安装和运行

### 1. 克隆或下载项目

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行应用
```bash
python app.py
```

### 4. 访问系统
打开浏览器访问: http://localhost:5000

## 项目结构

```
video-management-system/
├── app.py                 # 主应用文件
├── requirements.txt       # Python 依赖
├── README.md             # 项目说明
├── video_management.db   # SQLite 数据库（运行后自动创建）
├── templates/            # HTML 模板
│   ├── base.html        # 基础模板
│   ├── login.html       # 登录页面
│   ├── dashboard.html   # 仪表板
│   ├── videos.html      # 视频列表
│   ├── add_video.html   # 添加视频
│   └── edit_video.html  # 编辑视频
└── static/              # 静态文件
    └── uploads/         # 上传的视频文件
```

## 主要功能

### 管理员功能
- ✅ 添加新视频
- ✅ 编辑现有视频
- ✅ 归档视频
- ✅ 恢复归档视频
- ✅ 删除视频
- ✅ 搜索视频

### 视频存储方式
1. **本地上传**: 支持最大 500MB 的视频文件
2. **Google Drive**: 通过共享链接集成 Google Drive 视频

### 数据库设计
- **users 表**: 用户信息和权限
- **videos 表**: 视频信息、文件路径、Google Drive 链接等

## 技术栈

- **后端**: Flask (Python)
- **数据库**: SQLite
- **前端**: Bootstrap 5, Font Awesome, JavaScript
- **文件上传**: Werkzeug
- **安全**: 密码哈希、会话管理

## 安全特性

- 密码哈希存储
- 会话管理
- 文件上传安全检查
- 管理员权限验证
- CSRF 保护（通过 Flask 内置机制）

## 部署说明

### 生产环境配置
1. 更改 `app.secret_key` 为安全的随机字符串
2. 配置适当的数据库（如 PostgreSQL）
3. 设置环境变量
4. 使用 WSGI 服务器（如 Gunicorn）

### 环境变量
```bash
export FLASK_ENV=production
export SECRET_KEY=your-very-secure-secret-key
```

## 许可证

MIT License

## 支持

如有问题或建议，请创建 Issue 或联系开发团队。

---

**注意**: 这是一个演示项目，在生产环境中使用前请确保进行适当的安全配置和测试。
