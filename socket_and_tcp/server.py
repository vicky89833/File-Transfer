# Server
import socket
import os
def start_server(host='0.0.0.0', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            # Step 1: Receive filename length (fixed 4 bytes, big-endian integer)
            filename_len_bytes = conn.recv(4)
            filename_len = int.from_bytes(filename_len_bytes, 'big')

            # Step 2: Receive filename
            filename = conn.recv(filename_len).decode()
            print(f"Receiving file: {filename}")


            with open(filename, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print(f"File {filename} received successfully.")
start_server()
