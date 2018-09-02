#!/usr/bin/env python3
# encoding: utf-8
"""
@file: Student.py
@user: muyi-macpro
@time: 2018/4/6 上午11:58
@desc: 
"""


# 括号内代表继承object
class Student(object):
    # 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，
    # 这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
    # 当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

    # 双下划线开头的实例变量是不是一定不能从外部访问呢？
    # 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
    # 所以，仍然可以通过_Student__name来访问__name变量：

    def __init__(self, name, score):
        self.__name = name  # 私有变量
        self.__score = score  # 私有变量

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


if __name__ == '__main__':
    bob = Student('bob', 99)
    jim = Student('jim', 100)

    print(Student)
    print(bob)
    print(jim)
    # print(bob.__name)  # AttributeError: 'Student' object has no attribute '__name'
    # print(jim._Student__name)  # 99

    bob.print_score()
    jim.print_score()
