import socket
import os

def send_file(file_path, host='localhost', port=5000):
    filename = os.path.basename(file_path)
    filename_bytes = filename.encode()
    filename_len = len(filename_bytes)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Step 1: Send filename length
        s.sendall(filename_len.to_bytes(4, 'big'))

        # Step 2: Send filename
        s.sendall(filename_bytes)

        # Step 3: Send file data
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                s.sendall(data)

        print(f"File '{filename}' sent successfully!")

file_path = "/home/vicky/Downloads/B21BB033_LAB_3.pdf"
send_file(file_path)
