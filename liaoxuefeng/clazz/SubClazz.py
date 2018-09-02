#!/usr/bin/env python3
# encoding: utf-8
"""
@file: SubClazz.py
@user: muyi-macpro
@time: 2018/4/6 下午12:15
@desc: 
"""


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def eat(self):
        print('Cat is eating')


# 对于静态语言（例如Java）来说，如果需要传入Animal类型，
# 则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()

    dog.run()
    cat.run()

    run_twice(Dog())

    pass
