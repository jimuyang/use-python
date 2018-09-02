#!/usr/bin/env python3
# encoding: utf-8
"""
@file: CustomClazz.py
@user: muyi-macpro
@time: 2018/4/6 下午4:24
@desc: 
"""


# __slots__ 用于限制类的实例的属性
# __len__() 方法用于len()


class Student(object):
    def __init__(self, name):
        self.__name = name

    # 定制Student的__str__()
    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    # 在terminal环境下直接输出变量 调用的是__repr__()
    __repr__ = __str__


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, item):
        if isinstance(item, int):  # n是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # n是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


if __name__ == '__main__':
    jim = Student('jim')
    print(jim)  # <__main__.Student object at 0x10629b3c8>
    print(jim.__str__())  # <__main__.Student object at 0x10629b3c8>

    for n in Fib():
        print(n)

    print(Fib()[1])
    print(Fib()[1:5])

    pass
