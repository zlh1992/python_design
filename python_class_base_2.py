# -*- coding: utf-8 -*-
# @Time : 2021/11/10 下午2:04
# @Author : zhenglinghan
# @Email : zhenglinghan.zlh@antgroup.com
# @File : python_class_base_2.py
# @Project : python_design

from abc import ABCMeta, abstractmethod

# 抽象类
'''
抽象类是一个特殊的类，只能被继承，不能实例化，抽象类中可以有抽象方法和普通方法。

从实现角度来看，抽象类与普通类的不同之处在于：抽象类中有抽象方法，
该类不能被实例化，只能被继承！且子类必须实现抽象方法！
抽象类中可以定义普通的方法！
抽象类也是定义规范。
使用抽象类，子类一般都是单继承！
1.定义抽象类
定义抽象类需要导入 abc模块。from abc import ABCMeta, abstractmethod
'''


class Animal(metaclass=ABCMeta):

    # 抽象方法
    @abstractmethod  # 子类必须实现
    def eat(self): pass

    @abstractmethod
    def sleep(self): pass

    # 定义普通的方法
    def play(self):
        print('溜达...')


class Dog(Animal):

    def eat(self):
        print('吃骨头。。。')

    def sleep(self):
        print('默默地看门...')


dog = Dog()
dog.sleep()  # 默默地看门...
dog.play()  # 溜达...

'''
多态特性
多态就是不同子类对象调用父类的方法产生不同的结果。
对于抽象方法的不同实现
'''
# 使用不同的支付方式给商店付钱
import abc


class Pay(object):
    @abc.abstractmethod
    def pay(self, money): pass  ## 带参数的抽象方法


class Alipay(Pay):
    def pay(self, money):
        print('支付宝到账{}'.format(money))


class ApplePay(Pay):
    def pay(self, money):
        print('苹果支付{}'.format(money))


class Person(object):
    def consumption(self, pay, money):
        '''

        :param pay: 一个Pay类的对象
        :param money: 支付金额
        :return:
        '''
        pay.pay(money)


alipay = Alipay()
person = Person()
person.consumption(alipay, 1000)  # 支付宝到账1000
