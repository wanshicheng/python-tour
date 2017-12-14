import socket

import os

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)  # 3为排队的个数
print('waiting ...')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(1024)
        cmd, filename, file_size = str(data, 'utf8').split('|')
        path = os.path.join(BASE_DIR, 'img', filename)
        file_size = int(file_size)

        f = open(path, 'ab')

        has_receive = 0
        while has_receive != file_size:
            data = conn.recv(1024)
            f.write(data)
            f.flush()
            has_receive = len(data)
        f.close()


sk.close()
