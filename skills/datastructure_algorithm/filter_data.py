#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

from random import randint

data = [randint(-10, 10) for _ in range(10)]
print(data)

filter_data = filter(lambda x: x >= 0, data)
print(list(filter_data))

list_parse = [x for x in data if x >= 0]
print(list_parse)

# filter dict
scores = {x: randint(60, 100) for x in range(1, 21)}
print(scores)

good_students = {k: v for k, v in scores.items() if v > 90 }
print(good_students)

s = set(data)
print(s)
s = {x for x in s if x % 3 == 0}
