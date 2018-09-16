#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

from random import randint, sample

sample('abcdefg', 3)
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(1, 5))}

# 3个赛季的进球球员和进球数统计
s1, s2, s3 = ({x: randint(1, 4) for x in sample('abcdefg', randint(1, 5))} for _ in range(3))
print(s1, s2, s3)

res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print(res)

# 通过取交集的方式取到3个赛季都有进球的球员
s1.keys() & s2.keys() & s3.keys()

# 使用map reduce
s_keys = map(dict.keys, [s1, s2, s3])
# list(s_keys)

from functools import reduce
reduce(lambda a, b: a & b, s_keys)
