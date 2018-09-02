#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

p = (4, 5)
x, y = p

print(x, y)

data = ['AVMC', 50, 9.1, (2023, 14, 52)]
name, shares, price, date = data

print(name, shares, price, date)

year, month, day = date
print(year, month, day)

# 解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 
# 包括字符串，文件对象，迭代器和生成器。
