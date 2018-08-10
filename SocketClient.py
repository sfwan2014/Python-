#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

s = socket.socket()
host = socket.gethostbyname('127.0.0.1')
print host
port = 12334

s.connect((host, port))
print s.recv(1024)
s.close()
