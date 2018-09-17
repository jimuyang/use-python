#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 迭代器 切片
from itertools import islice
from collections import Iterable, Iterator 

f = open('/Users/muyi/Coding/vimtutor')
print(f)
print(isinstance(f, Iterable))

# for x in f:
#     print(x)

i1 = iter(f)
i2 = iter(f)
i3 = iter(f)

print(list(islice(i2, 2)))  # 1-2行
print(list(islice(i3, 2)))  # 3-4行 
print(list(islice(i1, 2)))  # 5-6行

'''
# file是一个特殊的Iterable 每次生成的迭代器好像共用浮标
print(list(islice(iter(f), 2)))
# print(list(islice(iter(f), 100, 102)))
print(list(islice(iter(f), 2)))
print(list(islice(iter(f), 2)))
'''


L = range(20)

t = iter(L)
print(list(islice(t, 5, 10)))
for x in t:
    print(x)
print(list(iter(L)))

