# encoding: utf-8
"""
@file: Iterator.py
@user: muyi-macpro
@time: 2018/4/1 下午2:40
@desc: python高级特性——迭代
"""
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for key, val in d.items():
    print(key, val)

# 只要是可迭代对象就可以用 for in 来遍历

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))

# 对数组实现下标循环
for index, value in enumerate(['a', 'b', 'c']):
    print(index, ':', value)

