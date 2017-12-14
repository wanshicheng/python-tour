import socket


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

        inp = input('>>>')
        conn.send(bytes(inp, 'utf-8'))

sk.close()
