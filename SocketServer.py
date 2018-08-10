#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

s = socket.socket()
host = socket.gethostbyname('127.0.0.1')
print host
port = 12334
s.bind((host, port))


s.listen(5)
while True:
    c, addr = s.accept()
    print '链接地址: ', addr
    c.send('欢迎访问菜鸟教程!')
    c.close()

