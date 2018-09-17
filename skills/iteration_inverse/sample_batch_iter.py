#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 在一个for循环中同时迭代多个可迭代对象

from random import randint

math_score = [randint(60, 100) for _ in range(40)]
english_score = [randint(60, 100) for _ in range(40)]
chinese_score = [randint(60, 100) for _ in range(40)]

# use index 不通用 
total_score = []
for i in range(len(math_score)):
    total_score.append(math_score[i] + english_score[i] + chinese_score[i])
print(total_score)

# use zip
z = zip([1, 2, 3, 4], ('a', 'b', 'c'), {'x', 'y', 'z'})
print(list(z))  # [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]

total_score = []
for m, c, e in zip(math_score, chinese_score, english_score):
    total_score.append(m + c + e) 
print(total_score)

from itertools import chain
# test
for x in chain([1, 2, 3, 4], ('a', 'b', 'c'), {'x', 'y', 'z'}):
    print(x)  # 注意这里发现 xyz的字典是无序的！

# 测试下字典是不是无序的
print('---test dict is ordered or not ')
for x in {'x', 'y', 'z'}:
    print(x)
print('---是的 这样创建的dict是无序的')

# 试下orderedDict
# from collections import OrderedDict
# d2 = {'x', 'y', 'z'}
# for x in OrderedDict(d2):
#     print(x)
# print('--OrderedDict')

d1 = {}
d1['x'] = 1
d1['y'] = 2
d1['z'] = 3
for x in d1:
    print(x)  # x y z 
print('-- 是的 这样的字典按照加入的顺序有序')


# 4个班级的英语成绩


