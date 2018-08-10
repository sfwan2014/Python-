#!/usr/bin/python
# -*- coding: UTF-8 -*-



try:
    fh = open("newdir/testfile", "w")
    fh.write("这是一个测试文件, 用于测试异常!")
except IOError:
    print "Error: 没有找到文件或读取文件失败!!"
else:
    print "内容写入文件成功"
    fh.close()

# import os
# path = os.getcwd()
# print path


try:
    fh = open("newdir/test.txt", "w")
    fh.write("这是一个测试文件, 用于测试异常!")
finally:
    print "Error: 没有找到文件或读取文件失败!!"




try:
    fh = open("newdir/testfile", "w")
    try:
        fh.write("这是一个测试文件, 用于测试异常!")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败!!"
