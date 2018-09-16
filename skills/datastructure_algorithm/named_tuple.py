#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

NAME, AGE, SEX = range(3)
# print(NAME, AGE, SEX)
student = ('jim', 14, 'male', 'jim43@gmail.com')

# name
print(student[0])

# age
print(student[1])

# sex
print(student[2])

from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
xiaoming = Student('jim', 14, 'male', 'jim43@gmail.com')
xiaogang = Student(name='xiaogang', age=15, sex='male', email='xiaogang@qq.com')
print(xiaoming.name)
print(xiaoming.age)
print(xiaogang.email)