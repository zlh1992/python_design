# -*- coding: utf-8 -*-
# @Time : 2021/11/8 下午11:20
# @Author : zhenglinghan
# @Email : zhenglinghan.zlh@antgroup.com
# @File : python_class_base_0.py
# @Project : python_design


'''
复习一下静态属性 动态属性
实例方法 静态方法 类方法
'''

'''
静态属性
'''


class Demo:
    type = "demo!"  # 静态 不定义对象都存在 可以通过对类修改 影响所有对象

    def __init__(self, day):
        self.day = "20211111"  # 实例化了对象才出现


d = Demo("20211111")
print(d.type)
print(d.day)
d.weather = "sunny"
print(d.weather)
d.day = "19991111"
d.type = "x"  # 对象 外部修改
print(d.type)  # 对象 外部修改生效
print(d.day)
Demo.month = 1
e = Demo("20211111")  # 类 外部修改
print(e.month)  # 所有对象都生效
print(d.month)  # 所有对象都生效


class Demo:
    __slots__ = ("day", "month")  # 不能包含class variable type slot对子类不起作用
    type = "demo!"

    def __init__(self, day):
        self.day = "20211111"


try:
    d = Demo("199911111")
    d.weather = "sunny"  # 已限定只能添加 day，month
except:
    d.month = "11"

'''
实例方法（instance method）：被类实例调用，第一个参数默认是self
静态方法(static method)：可以被类和实例调用，没有默认参数
类方法(class method)：可以被类和实例调用，第一个参数默认是类，一般用cls变量名
'''


class Demo:
    @staticmethod
    def write(x):
        print(x)


d = Demo()
d.write(1)
Demo.write(1)  # 静态方法


def eat1(x):
    print(f"eat1 {x}")


def eat2(x):
    print(f"eat2 {x}")


@staticmethod  # 静态方法
def test_static():
    print('aa')


@classmethod
def test_class(cls):  # 类方法
    print(cls.num)


def read(self, x):  # 实例方法
    print(f"read {x}")


d.eat1 = eat1
Demo.read = read

Demo.num = 1
Demo.test_static = test_static  # 添加静态方法
Demo.test_class = test_class  # 添加类方法
'''
a. 如果添加一个不带self参数的方法，可以直接通过 实例.方法名 的方式添加，也可以通过 类名.方法名添加 (无输入参数的方法)
b. 如果添加一个带self参数的方法，则只能通过类名.方法名来添加 （实例方法 类方法 静态方法）
'''
Demo.eat2 = eat2  # 没法用
'''
定义动态属性 内外部
'''
from types import MethodType


def read(self, x):
    print(f"read {x}")


d.read = MethodType(read, d)
d.read(2)  # 只对对象定义 新的方法 不影响同类的其他对象

'''
最后总结结论如下：
1. 动态添加实例属性：使用 对象名.新变量名 的方式
2. 动态添加类属性：使用 类.新变量名 的方式
3. 限制类的属性：__slots__
4. 静态方法与类方法：使用 类.新方法 的方式
5. 实例方法：
　　如果只对某个对象生效：使用types模块中的对象名.新方法名 = MethodType(function, 对象名) 的方式
　　如果对所有对象生效：使用 类.方法名 的方式
'''
