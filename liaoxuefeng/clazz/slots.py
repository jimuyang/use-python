#!/usr/bin/env python3
# encoding: utf-8
"""
@file: slots.py
@user: muyi-macpro
@time: 2018/4/6 下午12:35
@desc: 
"""
from types import MethodType


class People(object):
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
    pass


if __name__ == '__main__':
    # 给实例绑定属性
    p = People()
    p.name = 'jim'
    print(p.name)

    # 给实例绑定方法
    def set_age(self, age):
        self.age = age

    # p.set_age = set_age 这样不能正确的将self解释
    p.set_age = MethodType(set_age, p)  # 这里很像js bind？self很像js中的this
    p.set_age(35)
    print(p.age)

    # 给类绑定方法
    p2 = People()
    People.set_age_clazz = set_age
    p2.set_age_clazz(3)
    print(p2.age)

    p.set_age_clazz(5)
    print(p.age)

    # use __slots__ 限制class实例能添加的属性

    pass
