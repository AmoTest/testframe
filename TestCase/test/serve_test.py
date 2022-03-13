
import socket

# 一个小型服务器

s = socket.socket()

host = socket.gethostbyname("zhouwenxundeMacBook-Air.local")
port = 1234

s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print(f'Got connection from: {addr}')
    c.send("Thank You for connecting")
    c.close()