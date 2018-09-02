#!/usr/bin/env python3
# encoding: utf-8
"""
@file: collection.py
@user: muyi-macpro
@time: 2018/4/11 下午11:35
@desc: 
"""

from collections import namedtuple
from collections import deque
from collections import defaultdict

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x, p.y)

# deque是双向涟表
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

dq = deque([1, 23, 4])
dq.append(7)
dq.append('34t6')
dq.popleft()
print(dq)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在
print(dd['key2'])  # key2不存在，返回默认值
