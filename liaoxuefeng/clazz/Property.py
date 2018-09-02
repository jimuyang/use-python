#!/usr/bin/env python3
# encoding: utf-8
"""
@file: Property.py
@user: muyi-macpro
@time: 2018/4/6 下午4:16
@desc: 
"""
import numpy

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


if __name__ == '__main__':

    stu = Student()
    stu.score = 60
    print(stu.score)

    # stu.score = 101
    print(numpy)
    pass
