# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket

s = socket.socket()
host = socket.gethostname()
port = 5000
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('连接地址', addr)
    c.send('好耶'.encode('utf-8'))
    c.close()
