from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import sqlite3
import os
from datetime import datetime
import uuid
from config import config

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# 配置应用
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config.get(config_name, config['default']))

# 添加模板函数
@app.template_filter('is_expired')
def is_expired_filter(expiry_date):
    """检查视频是否过期"""
    return is_video_expired(expiry_date)

# 确保上传目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/js', exist_ok=True)

# 初始化数据库
def init_db():
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    
    # 用户表
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        is_admin BOOLEAN DEFAULT 1
    )''')
    
    # 视频表
    c.execute('''CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        filename TEXT,
        google_drive_url TEXT,
        google_drive_file_id TEXT,
        upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        expiry_date DATETIME,
        is_archived BOOLEAN DEFAULT 0,
        allow_download BOOLEAN DEFAULT 0,
        view_count INTEGER DEFAULT 0,
        created_by INTEGER,
        FOREIGN KEY (created_by) REFERENCES users (id)
    )''')
    
    # 创建默认管理员账户
    admin_password_hash = generate_password_hash('admin123')
    c.execute('''INSERT OR IGNORE INTO users (username, email, password_hash, is_admin) 
                 VALUES (?, ?, ?, ?)''', 
              ('admin', 'admin@example.com', admin_password_hash, True))
    
    conn.commit()
    conn.close()

# 检查用户是否已登录
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# 检查管理员权限
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        conn = sqlite3.connect('video_management.db')
        c = conn.cursor()
        c.execute('SELECT is_admin FROM users WHERE id = ?', (session['user_id'],))
        user = c.fetchone()
        conn.close()
        
        if not user or not user[0]:
            flash('需要管理员权限才能访问此页面', 'error')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# 检查视频是否过期
def is_video_expired(expiry_date):
    if not expiry_date:
        return False
    try:
        expiry = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
        return datetime.now() > expiry
    except:
        return False

# 提取 Google Drive 文件 ID
def extract_google_drive_file_id(url):
    if not url:
        return None
    
    # 处理不同格式的 Google Drive 链接
    import re
    
    # 匹配模式: https://drive.google.com/file/d/FILE_ID/view
    pattern1 = r'/file/d/([a-zA-Z0-9-_]+)'
    match = re.search(pattern1, url)
    if match:
        return match.group(1)
    
    # 匹配模式: https://drive.google.com/open?id=FILE_ID
    pattern2 = r'[?&]id=([a-zA-Z0-9-_]+)'
    match = re.search(pattern2, url)
    if match:
        return match.group(1)
    
    return None

# 生成受保护的 Google Drive 视频链接
def get_protected_video_url(file_id, allow_download=False):
    if not file_id:
        return None
    
    # 使用 Google Drive 嵌入播放器，禁止下载
    if allow_download:
        return f"https://drive.google.com/file/d/{file_id}/view"
    else:
        # 使用嵌入模式，更难下载
        return f"https://drive.google.com/file/d/{file_id}/preview"

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('video_management.db')
        c = conn.cursor()
        c.execute('''SELECT id, username, password_hash, is_admin 
                     FROM users 
                     WHERE username = ? OR email = ?''', 
                  (username_or_email, username_or_email))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['is_admin'] = user[3]
            flash('登录成功！', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('用户名/邮箱或密码错误', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('已成功退出登录', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    
    # 获取视频统计信息
    c.execute('SELECT COUNT(*) FROM videos WHERE is_archived = 0')
    active_videos = c.fetchone()[0]
    
    c.execute('SELECT COUNT(*) FROM videos WHERE is_archived = 1')
    archived_videos = c.fetchone()[0]
    
    # 获取最近的视频
    c.execute('''SELECT id, title, description, upload_date, google_drive_url, expiry_date 
                 FROM videos 
                 WHERE is_archived = 0 
                 ORDER BY upload_date DESC 
                 LIMIT 10''')
    recent_videos = c.fetchall()
    
    conn.close()
    
    return render_template('dashboard.html', 
                         active_videos=active_videos,
                         archived_videos=archived_videos,
                         recent_videos=recent_videos,
                         current_date=datetime.now().strftime('%Y-%m-%d'))

@app.route('/videos')
@login_required
def videos():
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    
    # 获取查询参数
    search = request.args.get('search', '')
    show_archived = request.args.get('archived', '0') == '1'
    
    query = '''SELECT id, title, description, filename, google_drive_url, upload_date, is_archived, expiry_date, allow_download, google_drive_file_id 
               FROM videos 
               WHERE is_archived = ? '''
    params = [1 if show_archived else 0]
    
    if search:
        query += ' AND (title LIKE ? OR description LIKE ?)'
        params.extend([f'%{search}%', f'%{search}%'])
    
    query += ' ORDER BY upload_date DESC'
    
    c.execute(query, params)
    videos = c.fetchall()
    conn.close()
    
    return render_template('videos.html', videos=videos, search=search, show_archived=show_archived)

@app.route('/add_video', methods=['GET', 'POST'])
@admin_required
def add_video():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        google_drive_url = request.form.get('google_drive_url', '')
        expiry_date = request.form.get('expiry_date', '')
        allow_download = 'allow_download' in request.form
        
        if not title:
            flash('视频标题不能为空', 'error')
            return render_template('add_video.html')
        
        # 提取 Google Drive 文件 ID
        google_drive_file_id = extract_google_drive_file_id(google_drive_url)
        
        # 验证过期日期
        if expiry_date:
            try:
                datetime.strptime(expiry_date, '%Y-%m-%dT%H:%M')
                # 转换为数据库格式
                expiry_date = datetime.strptime(expiry_date, '%Y-%m-%dT%H:%M').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                flash('过期日期格式不正确', 'error')
                return render_template('add_video.html')
        
        # 处理文件上传
        filename = None
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename:
                filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # 保存到数据库
        conn = sqlite3.connect('video_management.db')
        c = conn.cursor()
        c.execute('''INSERT INTO videos (title, description, filename, google_drive_url, google_drive_file_id, expiry_date, allow_download, created_by) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (title, description, filename, google_drive_url, google_drive_file_id, expiry_date or None, allow_download, session['user_id']))
        conn.commit()
        conn.close()
        
        flash('视频添加成功！', 'success')
        return redirect(url_for('videos'))
    
    return render_template('add_video.html')

@app.route('/edit_video/<int:video_id>', methods=['GET', 'POST'])
@admin_required
def edit_video(video_id):
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        google_drive_url = request.form.get('google_drive_url', '')
        
        c.execute('''UPDATE videos 
                     SET title = ?, description = ?, google_drive_url = ? 
                     WHERE id = ?''',
                  (title, description, google_drive_url, video_id))
        conn.commit()
        conn.close()
        
        flash('视频信息更新成功！', 'success')
        return redirect(url_for('videos'))
    
    # 获取视频信息
    c.execute('SELECT * FROM videos WHERE id = ?', (video_id,))
    video = c.fetchone()
    conn.close()
    
    if not video:
        flash('视频不存在', 'error')
        return redirect(url_for('videos'))
    
    return render_template('edit_video.html', video=video)

@app.route('/archive_video/<int:video_id>')
@admin_required
def archive_video(video_id):
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    c.execute('UPDATE videos SET is_archived = 1 WHERE id = ?', (video_id,))
    conn.commit()
    conn.close()
    
    flash('视频已归档', 'success')
    return redirect(url_for('videos'))

@app.route('/restore_video/<int:video_id>')
@admin_required
def restore_video(video_id):
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    c.execute('UPDATE videos SET is_archived = 0 WHERE id = ?', (video_id,))
    conn.commit()
    conn.close()
    
    flash('视频已恢复', 'success')
    return redirect(url_for('videos'))

@app.route('/watch_video/<int:video_id>')
@login_required
def watch_video(video_id):
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    
    # 获取视频信息
    c.execute('''SELECT id, title, description, google_drive_file_id, expiry_date, allow_download, view_count 
                 FROM videos 
                 WHERE id = ? AND is_archived = 0''', (video_id,))
    video = c.fetchone()
    
    if not video:
        flash('视频不存在或已被删除', 'error')
        return redirect(url_for('videos'))
    
    # 检查视频是否过期
    if is_video_expired(video[4]):
        flash('视频已过期，无法播放', 'error')
        return redirect(url_for('videos'))
    
    # 更新观看次数
    c.execute('UPDATE videos SET view_count = view_count + 1 WHERE id = ?', (video_id,))
    conn.commit()
    conn.close()
    
    # 生成受保护的视频链接
    protected_url = get_protected_video_url(video[3], video[5])
    
    return render_template('watch_video.html', video=video, video_url=protected_url)

@app.route('/delete_video/<int:video_id>')
@admin_required
def delete_video(video_id):
    conn = sqlite3.connect('video_management.db')
    c = conn.cursor()
    
    # 获取文件名以删除文件
    c.execute('SELECT filename FROM videos WHERE id = ?', (video_id,))
    video = c.fetchone()
    
    if video and video[0]:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], video[0])
        if os.path.exists(file_path):
            os.remove(file_path)
    
    c.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    conn.commit()
    conn.close()
    
    flash('视频已删除', 'success')
    return redirect(url_for('videos'))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 8081))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)
