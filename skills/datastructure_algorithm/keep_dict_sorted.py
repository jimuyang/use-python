#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 如何保持一个字典有序
d = {}

d['jim'] = (1, 35)
d['leo'] = (2, 45)
d['bob'] = (3, 54)

print(d.items())
for i in d:
    print(i)
# 从 python3.6开始 dict是有序的了


