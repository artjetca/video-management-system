import sys
import os
import json
from urllib.parse import unquote
from werkzeug.wrappers import Request, Response
from werkzeug.serving import WSGIRequestHandler
import tempfile

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# 设置临时目录用于文件上传
os.environ['TMPDIR'] = '/tmp'
os.makedirs('/tmp/uploads', exist_ok=True)

# 设置生产环境
os.environ['FLASK_ENV'] = 'production'

from app import app

def handler(event, context):
    """
    Netlify Functions handler for Flask app
    """
    try:
        # 获取请求信息
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        query_string = event.get('queryStringParameters') or {}
        headers = event.get('headers', {})
        body = event.get('body', '')
        
        # 如果是 POST 请求且有 body，解析 body
        if body and event.get('isBase64Encoded'):
            import base64
            body = base64.b64decode(body).decode('utf-8')
        
        # 构建环境变量
        environ = {
            'REQUEST_METHOD': http_method,
            'PATH_INFO': path,
            'QUERY_STRING': '&'.join([f'{k}={v}' for k, v in query_string.items()]),
            'CONTENT_TYPE': headers.get('content-type', ''),
            'CONTENT_LENGTH': str(len(body)) if body else '0',
            'SERVER_NAME': headers.get('host', 'localhost'),
            'SERVER_PORT': '443',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'https',
            'wsgi.input': body,
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
        }
        
        # 添加 HTTP 头到环境变量
        for key, value in headers.items():
            key = 'HTTP_' + key.upper().replace('-', '_')
            environ[key] = value
        
        # 创建 Flask 测试客户端
        with app.test_client() as client:
            # 构建查询字符串
            query_str = '&'.join([f'{k}={v}' for k, v in query_string.items()])
            full_path = path
            if query_str:
                full_path += '?' + query_str
            
            # 发送请求
            if http_method == 'GET':
                response = client.get(full_path, headers=headers)
            elif http_method == 'POST':
                response = client.post(full_path, data=body, headers=headers)
            elif http_method == 'PUT':
                response = client.put(full_path, data=body, headers=headers)
            elif http_method == 'DELETE':
                response = client.delete(full_path, headers=headers)
            else:
                response = client.open(full_path, method=http_method, data=body, headers=headers)
            
            # 构建响应
            response_headers = {}
            for key, value in response.headers:
                response_headers[key] = value
            
            return {
                'statusCode': response.status_code,
                'headers': response_headers,
                'body': response.get_data(as_text=True)
            }
            
    except Exception as e:
        print(f"Error in Netlify function: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Internal server error', 'message': str(e)})
        }
