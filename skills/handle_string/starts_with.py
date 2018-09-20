#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 判断字符串是否以一个字符串开头

L = ['a.sh', 'b.py', 'c.cpp']

import os
print(os.listdir())  # ['cookbook', '.gitignore', 'skills', 'venv', '.git', '.vscode', 'liaoxuefeng', 'bitcoin-price']

string = 'sfe.py'
print(string.endswith('.py'))

# endswith startswith 可以传入一个元组
count = 0
for x in L:
    if x.endswith(('.sh', '.py', '.cpp')):
        count += 1
    if x.startswith(('a', 'b', 'c')):
        count += 1
print(count)

