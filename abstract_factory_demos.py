# -*- coding: utf-8 -*-
# @Time : 2021/11/10 下午3:52
# @Author : zhenglinghan
# @Email : zhenglinghan.zlh@antgroup.com
# @File : abstract_factory_demos.py
# @Project : python_design


from abc import ABCMeta, abstractmethod

"""
简单的工厂模式
"""


class Animal(metaclass=ABCMeta):
    """
    抽象类
    """

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


class ForestFactory(object):
    """
    工厂类
    主入口 调用不同的工厂产物的不同方法
    """

    def make_sound(self, object_type):
        """

        :param object_type: 是animal类的一个对象 str
        :return:
        """
        return eval(object_type)().do_say()


"""
工厂模式
"""


class Section(metaclass=ABCMeta):
    """
    内容抽象类
    """

    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatenSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    """
        公司抽象类
    """

    def __init__(self):
        """
        初始化自身的属性
        初始化的时候直接把内容加入到这个sections
        """
        self.sections = []  # 存内容对象
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        """
        获取
        给子类继承
        :return:
        """
        return self.sections

    def addSections(self, section):
        """
        添加
        给子类继承
        :param section:
        :return:
        """
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatenSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


"""
抽象工厂模式
"""


class PizzFactory(metaclass=ABCMeta):
    """
    抽象的披萨店
    可以卖荤 素两种披萨
    """

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class VegPizza(metaclass=ABCMeta):
    """
    抽象的素披萨
    """

    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    """
    抽象的荤披萨
    """

    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    """
        素
    """

    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    """
        荤
    """

    def serve(self, VegPizza):
        """

        :param VegPizza: 一个素披萨对象
        :return:
        """
        print(type(self).__name__, " is served with Chicken on", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    """
        素
    """

    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):
    """
        荤
    """

    def serve(self, VegPizza):
        """

        :param VegPizza: 一个素披萨对象
        :return:
        """
        print(type(self).__name__, " is served with Ham on", type(VegPizza).__name__)


class IndianPizzaFactory(PizzFactory):
    "印式披萨"

    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzFactory):
    "美式披萨"

    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class PizzaStore:
    """
    整合工厂
    """

    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()  # 素的直接perpare
            self.NonVegPizza.serve(self.VegPizza)  # 混的陪素的


if __name__ == '__main__':
    """
    demo 1
    """
    print("demo 1")
    ff = ForestFactory()
    animal = input("Which animal should make_sound?[Dog or Cat]")
    ff.make_sound(animal)

    """
    demo 2
    """
    print("demo 2")
    profile_type = input("Which Profile you`d like to create?[LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
    for i in profile.getSections():
        i.describe()

    """
    deom3
    """
    print("demo 3")
    pizza = PizzaStore()
    pizza.makePizzas()

    '''
    总结：
    工厂方法：一个创建对象的方法，使用继承和子类决定要创建什么对象 用于创建一个产品
    抽象工厂方法：包含一系列多个工厂方法，使用组合讲创建对象的任务委托给别的类 用于创建一个系列的产品
    '''
