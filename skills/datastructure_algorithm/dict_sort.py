#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

sorted([1, 5, 0, 9])

from random import randint
dic = {x: randint(60, 100) for x in 'xyczaowv'}
sorted(dic)   # ['a', 'c', 'o', 'v', 'w', 'x', 'y', 'z']

(97, 'a') > (97, 'b')

for x in zip(dic.values(), dic.keys()):
    print(x)

zip(dic.values(), dic.keys())
list(zip(dic.values(), dic.keys()).__iter__())
list(zip(dic.values(), dic.keys()))
zip(dic.values(), dic.keys()).__iter__()

from collections import Iterable, Iterator
zip_res = zip(dic.values(), dic.keys())
isinstance(zip_res, Iterable)
isinstance(zip_res, Iterator)

zip_res.__next__()

sorted(zip(dic.values(), dic.keys()))
sorted(dic.items(), key=lambda x: x[1], reverse=True)
