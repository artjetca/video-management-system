# 🔧 Railway 环境变量设置详细指南

## 📋 什么是环境变量？

环境变量是应用程序运行时需要的配置信息，用于：
- `FLASK_ENV=production` - 告诉 Flask 这是生产环境
- `SECRET_KEY` - 用于会话加密和安全功能

## 🚂 在 Railway 中设置环境变量

### 步骤 1：部署完成后进入项目
1. 在 Railway 仪表板中，找到您的项目
2. 项目名称可能是：`video-management-system` 或类似名称
3. **点击项目卡片**进入项目详情页面

### 步骤 2：找到环境变量设置
在项目页面中，您会看到几个标签：
- **Deployments** (部署)
- **Variables** (变量) ← **点击这个**
- **Settings** (设置)
- **Metrics** (指标)

**点击 "Variables" 标签**

### 步骤 3：添加第一个环境变量
1. 在 Variables 页面，您会看到一个输入框
2. 点击 **"New Variable"** 或 **"Add Variable"** 按钮

#### 添加 FLASK_ENV：
- **Variable Name (变量名)**：输入 `FLASK_ENV`
- **Value (值)**：输入 `production`
- 点击 **"Add"** 或 **"Save"** 按钮

### 步骤 4：添加第二个环境变量
重复上述步骤：

#### 添加 SECRET_KEY：
- **Variable Name (变量名)**：输入 `SECRET_KEY`
- **Value (值)**：输入 `mi-clave-secreta-super-segura-12345`
- 点击 **"Add"** 或 **"Save"** 按钮

### 步骤 5：验证设置
设置完成后，您应该看到：

```
FLASK_ENV = production
SECRET_KEY = mi-clave-secreta-super-segura-12345
```

## 🔄 重新部署（如果需要）

设置环境变量后：
1. Railway 通常会**自动重新部署**应用
2. 如果没有自动重新部署，您可以：
   - 在 **Deployments** 标签中点击 **"Redeploy"**
   - 或者推送一个小的代码更改到 GitHub

## 🎯 完整的设置截图说明

### Railway 界面布局：
```
┌─────────────────────────────────────────┐
│  Railway Dashboard                      │
├─────────────────────────────────────────┤
│  Your Projects:                         │
│  ┌─────────────────────────────────────┐ │
│  │ video-management-system             │ │
│  │ ● Active                            │ │
│  │ https://your-app.railway.app        │ │
│  └─────────────────────────────────────┘ │ ← 点击这个项目
└─────────────────────────────────────────┘
```

### 项目详情页面：
```
┌─────────────────────────────────────────┐
│ video-management-system                 │
├─────────────────────────────────────────┤
│ [Deployments] [Variables] [Settings]    │ ← 点击 Variables
├─────────────────────────────────────────┤
│ Environment Variables:                  │
│                                         │
│ [+ New Variable]  ← 点击添加新变量        │
│                                         │
│ Name: [FLASK_ENV        ]               │
│ Value: [production      ]               │
│ [Add Variable]                          │
└─────────────────────────────────────────┘
```

## ⚠️ 重要注意事项

### SECRET_KEY 安全性：
- **不要使用示例中的密钥**！
- 建议生成一个更安全的密钥：

#### 生成安全密钥的方法：
```python
# 在 Python 中运行：
import secrets
print(secrets.token_hex(32))
```

或者使用在线生成器：
- 访问 https://randomkeygen.com/
- 选择 "CodeIgniter Encryption Keys" 或类似选项

### 推荐的安全 SECRET_KEY：
```
SECRET_KEY=a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456
```

## 🔍 验证环境变量是否生效

设置完成后，访问您的应用：
1. 打开 Railway 提供的 URL
2. 如果能正常登录，说明环境变量设置成功
3. 如果出现错误，检查：
   - 变量名是否正确（区分大小写）
   - 值是否正确输入
   - 是否已重新部署

## 🆘 常见问题

### Q: 找不到 Variables 标签？
A: 确保您点击的是项目本身，而不是部署记录

### Q: 设置后应用仍然报错？
A: 
1. 检查部署日志中的错误信息
2. 确保变量名完全正确
3. 尝试手动触发重新部署

### Q: SECRET_KEY 应该多长？
A: 建议至少32个字符，包含字母和数字

## 📞 需要帮助？

如果遇到问题，请提供：
1. Railway 项目的截图
2. Variables 页面的截图
3. 任何错误信息

---

**设置完成后，您的西班牙语视频管理系统就可以正常运行了！** 🎉
