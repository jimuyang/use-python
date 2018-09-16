#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

from random import randint
list = [randint(0, 21) for _ in range(20)]
print(list)

c = dict.fromkeys(list, 0)
print(c)

for x in list:
    c[x] += 1

print(c)

# use collections Counter
from collections import Counter
c1 = Counter(list)
print(c1)

print(c1.most_common(3))

import os, re

print(os.getcwd())
# file = open('filter_data.py').read()

# 统计文件中词频最高的单词
with open('/Users/muyi/Coding/Github/use-python/skills/filter_data.py', 'r') as file:
    txt = file.read()
    c2 = Counter(re.split('\W+', txt))
    print(c2)
    most_common_words = c2.most_common(3)
    print(most_common_words)
    # print(file.read())
print(os.getcwd)

