# -*- coding: utf-8 -*-
# @Time : 2021/11/8 下午10:57
# @Author : zhenglinghan
# @Email : zhenglinghan.zlh@antgroup.com
# @File : abstract_py.py
# @Project : python_design

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}!"
        print(msg)


class Bug:
    def __str__(self):
        return "a bug"

    def action(self):
        return "eat it!"


# 用抽象工厂FrogWorld 创建游戏重的主角与障碍物
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t-----Frog World-----"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstracle(self):
        return Bug()


f = FrogWorld("frog")
f.make_character()
f = FrogWorld("bug")
f.make_obstracle()
