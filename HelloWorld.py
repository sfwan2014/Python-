#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "hello world 时间";

if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    print "False"


word = 'word'
sentence = "这是一个句子."
paragraph = """这是一个段落.
包含了多个语句"""

# 注释
print paragraph     # 注释

'''
这是多行注释, 使用单引号
这是多行注释, 使用单引号
这是多行注释, 使用单引号
'''

"""
这是多行注释, 使用单引号
这是多行注释, 使用单引号
这是多行注释, 使用单引号
"""


# raw_input("按下enter.一旦按下 enter 键退出,其他键显示")



x = 'a'
y = 'b'

# 换行输出
print x
print y

print '--------------------'

# 不换行输出 以逗号(,)隔开
print x,
print y,


# 不换行输出
print x, y



a = b = c = 1

print a, b, c

a , b, c = 1, 2, 'jhon'
print a, b, c



fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果: ', fruits[index]

print "Good bye"


for fruit in fruits:
    print '当前水果: ', fruit
print "Good bye"




import time;

ticks = time.time()
print ticks;

localtime = time.asctime(time.localtime(ticks))
print localtime

date = time.strftime("%Y-%m-%d %H:%M:%S" ,time.localtime(ticks))
print date;







