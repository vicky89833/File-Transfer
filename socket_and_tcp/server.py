# Server
import socket

def start_server(host='0.0.0.0', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            with open('received_file', 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print("File received successfully")
