import socket
import subprocess


sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)  # 3为排队的个数
print('waiting ...')

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        print('...', str(data, 'utf-8'))
        if not data:
            break
        print(str(data, 'utf-8'))
        popen = subprocess.Popen(str(data, 'utf-8'), shell=True, stdout=subprocess.PIPE)
        cmd_result = popen.stdout.read()
        result_len = len(cmd_result)

        conn.sendall(bytes(str(result_len), 'utf-8'))

        conn.recv(1024)

        conn.sendall(cmd_result)
        print(str(cmd_result, 'gbk'))

sk.close()
