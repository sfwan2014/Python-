#!/usr/bin/python
# -*- coding: UTF-8 -*-


fo = open("foo.txt", "a+")
fo.write("www.runoob.com!\n very good site! \n")
fo.close()

fo = open("foo.txt", "r+")
str = fo.read()
print str

position = fo.tell()
print "当前文件位置: ", position

position = fo.seek(0, 0)


str1 = fo.read(20)
fo.close()

print str1



# 重命名
import os
os.rename("foo.txt", "fooo.txt")
cwd= os.getcwd()    # 获取当前路径
print cwd
path = cwd+"/newdir"    # 目标路径
print path
if not(os.path.exists(path)):   # 目标路径是否存在
    os.mkdir("newdir")      # 不存在 则创建
filepath = cwd + "/newdir/test.txt"     # 文件路径
fo = open(filepath, "a+")       # 打开文件
fo.write("hello world!\n")      # 写入文件
fo.close()

