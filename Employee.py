#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    # 构造函数
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # 析构函数
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, ": ", self.name, "销毁"

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, "  Salary: ", self.salary

Jhon = Employee("Jhon", 12000)
# em.displayCount()
Jhon.displayEmployee()

Stive = Employee("Stive", 13000)

Stive.displayEmployee()

bob = Employee("Bob", 8000)

bob.displayEmployee()

Jhon.displayCount()

Stive.age = 20
Jhon.age = 23
bob.age = 29

print "Jhon age is : ", Jhon.age


if hasattr(bob, 'age'):
    age = getattr(bob, 'age')
    print "bob age: ", age
else:
    setattr(bob, 'age', 8)

print "Bob real age: ", bob.age


"""
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""

print "Employee.__doc__: ", Employee.__doc__
print "Employee.__dict__: ", Employee.__dict__
print "Employee.__name__: ", Employee.__name__
print "Employee.__module__: ", Employee.__module__
print "Employee.__bases__: ", Employee.__bases__

"""
类的继承
"""
class ComputeEmployee (Employee):

    cer = "Compute Cer"

    def displayEmployee(self):
        print "Name: ", self.name, "  Salary: ", self.salary, "Cer: ", self.cer


computer = ComputeEmployee("Jobs", "30000")

computer.displayEmployee()


# 重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -3)

print v1+v2




# 类的私有属性
"""
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods

类的protected修饰
_protected_method/_protected_attrs: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import 
"""

class JustCounter:
    __secretCount = 0   # 私有变量
    publicCount = 0     # 公开变量
    _protectedCount = 0     # 保护变量

    # 私有方法
    def __counter(self):
        self.__secretCount += 1
        self.publicCount += 1
        self._protectedCount += 1
        print self.__secretCount

    def count(self):
        self.__counter()


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter._protectedCount

# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）
print counter._JustCounter__secretCount




