import socket
import threading
import os
import json

HOST = '0.0.0.0'
PORT = 8080

def handle_client(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8')
    if not request_data:
        client_socket.close()
        return

    request_line = request_data.splitlines()[0]
    print(f"[LOG] Yeni istek: {request_line}")  # LOG

    try:
        method, path, _ = request_line.split()
    except ValueError:
        client_socket.close()
        return

    # ---- POST /api/echo ----
    if method == 'POST' and path == '/api/echo':
        body = request_data.split('\r\n\r\n', 1)[1] if '\r\n\r\n' in request_data else ''
        response_body = json.dumps({'received': body}).encode('utf-8')
        response = (
            'HTTP/1.1 200 OK\r\n'
            'Content-Type: application/json\r\n'
            f'Content-Length: {len(response_body)}\r\n'
            '\r\n'
        ).encode('utf-8') + response_body

    # ---- GET /static/... ----
    elif method == 'GET' and path.startswith('/static/'):
        file_path = '.' + path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            if file_path.endswith('.html'):
                content_type = 'text/html'
            elif file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'
            else:
                content_type = 'application/octet-stream'
            response = (
                f'HTTP/1.1 200 OK\r\n'
                f'Content-Type: {content_type}\r\n'
                f'Content-Length: {len(content)}\r\n'
                f'\r\n'
            ).encode('utf-8') + content
        else:
            response_body = '<h1>404 - Dosya Bulunamadı</h1>'.encode('utf-8')
            response = (
                f'HTTP/1.1 404 Not Found\r\n'
                f'Content-Type: text/html\r\n'
                f'Content-Length: {len(response_body)}\r\n'
                f'\r\n'
            ).encode('utf-8') + response_body

    # ---- GET /api/hello ----
    elif method == 'GET' and path == '/api/hello':
        data = {'message': 'Merhaba!'}
        content = json.dumps(data).encode('utf-8')
        response = (
            f'HTTP/1.1 200 OK\r\n'
            f'Content-Type: application/json\r\n'
            f'Content-Length: {len(content)}\r\n'
            f'\r\n'
        ).encode('utf-8') + content

    # ---- GET / ----
    elif method == 'GET' and path == '/':
        response_body = '<h1>Python Web Sunucu Çalışıyor</h1>'.encode('utf-8')
        response = (
            f'HTTP/1.1 200 OK\r\n'
            f'Content-Type: text/html\r\n'
            f'Content-Length: {len(response_body)}\r\n'
            f'\r\n'
        ).encode('utf-8') + response_body

    # ---- 404 ----
    else:
        response_body = '<h1>404 - Sayfa Bulunamadı</h1>'.encode('utf-8')
        response = (
            f'HTTP/1.1 404 Not Found\r\n'
            f'Content-Type: text/html\r\n'
            f'Content-Length: {len(response_body)}\r\n'
            f'\r\n'
        ).encode('utf-8') + response_body

    client_socket.sendall(response)
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[INFO] Sunucu {PORT} portunda dinleniyor...")

    while True:
        client_conn, _ = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_conn,)).start()

if __name__ == '__main__':
    start_server()
