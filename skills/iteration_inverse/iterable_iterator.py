#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 可迭代对象
L = [1, 3, 5, 7]
string = 'asdfasf'

# 数组和字符串都是可迭代对象
for x in L: print(x)
for x in string: print(x)

print(iter(L))
print(L.__iter__())

print(iter(string))
print(string.__iter__())
# print(string.__getitem__())
