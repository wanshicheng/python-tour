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

    data = sk.recv(1024)
    print(str(data, 'utf-8'))

sk.close()