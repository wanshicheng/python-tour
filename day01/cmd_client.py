import socket


sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)
# data = sk.recv(1024)
# print(str(data, 'utf-8  '))

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf-8'))
    result_len = int(str(sk.recv(1024), 'utf-8'))
    sk.sendall(bytes('ok', 'utf-8'))
    print(int(result_len))

    data = bytes()
    while len(data) != result_len:
        recv = sk.recv(1024)
        data += recv

    print(str(data, 'gbk'))

sk.close()