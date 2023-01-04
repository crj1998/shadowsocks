# -*- coding: utf-8 -*-
# 2017/11/25 22:55
import socket
client = socket.socket()
client.connect(('127.0.0.1', 9000))
while True:
    cmd = input('>>> ').strip()
    if len(cmd) == 0 : continue
    if cmd == "close": break
    client.send(cmd.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())
client.close()