#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 队列的使用 双向队列

from collections import deque
que = deque([], 5)
for x in range(0, 10):
    que.append(x)
print(que)

que.appendleft(10)
print(que)

s = ''
print(s | 'sasd')