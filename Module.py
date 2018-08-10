#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
模块的声明及使用
"""

import Function
# from Function import sumall

sum1 = Function.sumall(5,2,4)
print sum1

dirContent = dir(Function)
print dirContent


str = raw_input("输入...")
print "输入的内容: ", str