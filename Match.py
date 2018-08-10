#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    正则表达式

"""

import re;
print re.match('www', 'www.runoob.com').span()
print re.match('com', 'www.runoob.com')

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"


# match 与search 的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search(r'dogs', line, re.M|re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

s = "110223199002231231"
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
print res.groupdict()

# 检索和替换
# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项

phone = "2004-985-234 # 这是一个国外电话号码"

# 删除字符串中的Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是: ", num

# repl 参数是一个函数
# 将匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

s = "A23G4HFD567"
print re.sub('(?P<value>\d+)', double, s)


# re.compile
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
pattern = re.compile(r'\d+')
m = pattern.match("one123twothree4four")
print m

m = pattern.match("one123twothree4four", 2, 10)
print m

m = pattern.match("one123twothree4four", 3, 10)
print m.group(0)
print m.start(0)
print m.end(0)
print m.span(0)


# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

pattern = re.compile(r'\d+')
result1 = pattern.findall("runoob 123 google 232")
result2 = pattern.findall("run99oob123google456", 0, 10)
print result1[0]
print result2

# re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r'\d+', "12ad32df456rt2")
for match in it:
    print match.group()

# splite
# split 方法按照能够匹配的子串将字符串分割后返回列表

res = re.split('\W+', 'runoob, runoob, runoob.')
print res

