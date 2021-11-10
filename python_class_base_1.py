# -*- coding: utf-8 -*-
# @Time : 2021/11/8 下午11:20
# @Author : zhenglinghan
# @Email : zhenglinghan.zlh@antgroup.com
# @File : python_class_base_1.py
# @Project : python_design

'''
python继承、多态---子类和父类、super()、派生、抽象类、多继承、多态特性

一、继承特性

1.什么是继承?

2.继承中子类和父类的概念

3.继承的作用

4. 查看继承的父类

 5.方法的复写

6.super()

 7.__init__()方法

8. 派生属性

9.私有属性私有方法在继承中的表现

10.抽象类

 二、多继承

1、语法

3、继承原理(钻石继承)

4、多继承中super本质

三、多态特性

'''

'''
一、继承特性
1.什么是继承?
继承就是让类和类之间产生父子关系，子类可以拥有父类的静态属性和方法。

继承就是可以获取另外一个类中的静态属性和普通方法。(并非所有成员)

在python中，新建的类可以继承一个或多个父类，父类又可称为基类或超类，新建的类称为派生类或子类。

注意：python中的继承分为：单继承和多继承。

2.继承中子类和父类的概念
父类:用于被继承的类，称之为父类，也叫做基类，或者超类。

子类:继承其他类的类，称之为子类，也叫做派生类。

3.继承的作用
提高代码的重用率

练习1：创建Dog类和Cat类，分别设置name,age属性和定义eat()、sleep()方法。

并且Dog类在定义一个look_door()方法，Cat类定义climb_tree()方法。
'''


class Animal(object):
    type = "动物"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃饭")

    def sleep(self):
        print("睡觉")

    def __drink__(self):
        print("喝水")

    def __group(self):
        self.age += 1


class Dog(Animal):

    def look_door(self):
        print("看门🐶")


class Cat(Animal):

    def climb_tree(self):
        print("爬🌲")


dog1 = Dog("京东狗", 8)
dog2 = Dog("柴犬", 4)
dog1.eat()
dog2.eat()
dog1.__drink__()
dog2.sleep()
dog1.look_door()
dog2.look_door()
try:
    dog1._group()  # 似有方法不能被继承
except:
    dog1.age += 1
    print(dog1.age)

'''
4. 查看继承的父类 
格式：类名.__bases__
'''
print(Dog.__bases__)  # 查看父类

'''
5.方法的复写
子类中定义了和父类中相同的方法，我们叫做方法的复写（派生方法）。实例对象调用此方法 的时候就会调用自己类中的方法了。
'''


class Pig(Animal):

    def eat(self):
        print('吃猪饲料')


pig = Pig('荷兰猪', 3)
pig.eat()  # 吃猪饲料

'''
6.super()
子类和父类有相同的方法，如果子类想调用父类相同的的方法。可以使用super()方法。

在python3中，子类执行父类的方法也可以直接用super方法 --->super()

super默认省略了两个参数 第一个参数是类名，第二个参数是self。两个参数可以省略不传递例如 super(Student,self)

super()还可以从类的外部使用 需要传递类名(本类的名称)和对象名

例如 super(Student,student)

格式：

父类类名.方法名称(self) 或者 super().方法名称()或者super(本类类名,对象名)
'''


class Dog(Animal):

    def sleep(self):
        # 方法一 父类.方法名(对象)
        # Animal.eat(self)
        # 方法二 super(子类,对象名).方法名()
        super(Dog, dog).sleep()  # 先调用了父类方法sleep
        print('去狗窝')

    def look_door(self):
        print('看门狗')


dog = Dog('哈巴狗', 23)
dog.sleep()
super(Dog, dog).sleep()  # 类Dog 对象dog 父类的方法sleep
try:
    print(super(Dog, dog).name)  # 属性不行
except:
    print(dog.name)
'''
睡觉
去狗窝
'''

'''
7.__init__()方法 
- 子类继承父类，如果子类不复写父类的__init__()方法，

   创建子类对象的时候会自动调用父类__init__()方法。

 - 子类继承父类，如果子类复写了父类的__init__()方法，

   创建的子类对象的时候不会再调用父类的__init__() 方法。

 - 注意：python要求复写父类的__init__()方法时，需要调用父类的__init__()

   因为存在隐患，例如父类的初始化方法有参数，子类初始化无参数，子类再调用父类的参数的时候就会报错。
'''


class Perpon:
    def __init__(self, name):
        print('person...')
        self.name = name


class Student(Perpon):
    def __init__(self):
        print('student...')


try:
    student = Student()
    print(student.name)  # 报错
except:
    pass


# 如果子类不复写父类的__init__()方法,就默认用父类的
# 如果复写，就值只用自己的,不建议使用
class Perpon:
    def __init__(self):
        self.age = 8
        print('person...')

    def run(self):
        print("run")


class Student(Perpon):
    def __init__(self):
        # super().__init__()
        print('student...')


try:
    student = Student()  # student...
    print(student.age)  # 因为子类自己初始化，不再继承父类的属性
except:
    student = Student()  # student...
    student.run()  # 方法依旧继承


class Student(Perpon):
    def __init__(self):
        super().__init__()
        print('student...')


student = Student()  # student...
print(student.age)  # 调用了父类的初始化，继承了父类的属性
student.run()


class Perpon:
    def __init__(self, age):
        self.age = age
        print('person...')

    def run(self):
        print("run")


class Student(Perpon):
    def __init__(self, age):
        super().__init__(age=age)
        print('student...')


student = Student(10)  # student...
print(student.age)  # 调用了父类的初始化，继承了父类的属性 父类初始化有参数，子类也需要
student.run()

'''
8. 派生属性
属性的覆盖(派生属性)：子类也可以添加自己新的属性或者在自己这里重新定义这些属性（不会影响到父类），需要注意的是，一旦重新定义了自己的属性且与父类重名，那么调用新增的属性时，就以自己为准了(属性的覆盖)。
'''


# 派生属性: 子类中自己添加的新属性
# 属性的覆盖: 子类和父类有相同属性,调用自己的
class Perpon:
    num = 20

    def __init__(self, name):
        print('person...')


class Student(Perpon):
    num = 10  # 把父类中的20覆盖

    def __init__(self, name, age):  # age 为派生属性
        super().__init__(name)
        self.name = name
        self.age = age
        print('student...')

    def study(self):
        print(super().num)
        pass


'''
9.私有属性私有方法在继承中的表现
父类中的私有方法和私有属性都是不能被子类继承下来的。
'''


class Perpon:
    num = 20
    __num1 = 12

    def __test1(self):
        print('__test1....')

    def test2(self):
        print('test2...')


class Student(Perpon):

    def test(self):
        print('num...')
        try:
            print(Student.__num1)
        except:
            print(self.num)
        try:
            self.__test1()
        except:
            self.test2()


s = Student()
s.test()

'''
多继承
一个子类可以继承多个父类，就是多继承，并且拥有所有父类的属性和方法
'''


class A(object):
    num_a = 1

    def test1(self):
        print('A--test1')

    def test2(self):
        print('A--test2')


class B(object):
    num_b = 2

    def test3(self):
        print('B--test3')

    def test4(self):
        print('B--test4')


class C(A, B):
    def test5(self):
        print('C--test5')


c = C()
c.test1()  # A--test1
c.test2()  # A--test2
c.test3()  # B--test3
c.test4()  # B--test4
print(c.num_a)  # 1
print(c.num_b)  # 2
c.test5()  # C--test5

'''
2、多继承注意事项
如果子类和父类有相同的方法，就会调用子类中的方法。
如果不同的父类中存在着相同的方法名称，子类对象调用的时候会调用哪个父类中的方法呢? Python会根据 MRO(method resolution order) 方法解析顺序列表进行查找。
提示：开发时，需要避免这种容易产生混淆的情况！--如果父类之间存在同名的属性和方法，应尽量避免使用多继承。
'''


class A(object):
    def test(self):
        print('A--test')


class B(A):
    def test(self):
        super().test()

        print('B--test')


class C(A):
    def test(self):
        super().test()

        print('C--test')


class D(B, C):
    def test(self):
        super().test()
        print('D--test')


d = D()
d.test()  # 广度优先 找到父类
