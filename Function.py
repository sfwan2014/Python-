#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
函数是使用及声明
'''

def testFunc():
    print "testFunc called"

testFunc()


def testFunc(str):
    print "testFunc called str: ", str

testFunc("Hello")




# 不可变参数  strings, tuples, 和 numbers

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)

print b

# 可变参数 list  dictionary
def ChangeList(myList):
    myList.append([1,3,2,4])
    print "函数内部取值: ", myList
    return

myList = [10,20,30]
ChangeList(myList)
print "函数外部取值: ", myList


# 关键字参数   参数名需与调用时关键字一致
def printme(str):
    print str
    return

printme(str = "My string")

# 关键字的顺序不重要
def printinfo(name, age):
    print "Name: ", name
    print "Age: ", age
    return

printinfo(age = 40, name="Dbc")

# 缺省参数
def printTick(name, no = 1001):
    print "Name: ", name
    print "No: ", no
    return

printTick("Dave", 1002)
printTick("Jhon")
printTick(name="Stive")
printTick(name="Bob", no=1003)


# 不定长参数
def printmoreinfo(arg1, *vartruple):
    print "输出"
    print arg1
    for var in vartruple:
        print var
    return

printmoreinfo(10)
printmoreinfo(70, 60, 50, 40, 30, 20, 10)


def sumall(*vars):
    s=0
    for var in vars:
        s+=var
    return s

s = sumall(1,2,3,4,5,6,7,8,9,10)
print "1+2+3+4+5+6+7+8+9+10=",s

# 匿名函数

sum = lambda arg1, arg2: arg1+ arg2

print sum(10,290)
print sum(20,300)


# 局部变量与全局变量
total = 0 # 全局变量
def suma(arg1, arg2):
    total = arg1+arg2 # 局部变量
    print "函数内是局部变量: ", total
    return total

suma(1,2)
print "函数外是全局变量: ", total


# 全局变量要在函数内使用, 需用global 修饰

money = 10

def AddMoney():
    global money
    money = 10 + 10
    return

print "Money: ", money

AddMoney()

print "Money: ", money


def descFunc():
    '''
        解释函数的用途,及参数使用
    '''
    pass
print (descFunc.__doc__)



