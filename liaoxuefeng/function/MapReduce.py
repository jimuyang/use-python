# encoding: utf-8
"""
@file: MapReduce.py
@user: muyi-macpro
@time: 2018/4/2 下午11:18
@desc: map() 和 reduce()
"""
from collections import Iterable, Iterator
from functools import reduce


# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


# 一个函数
def pingfang(x):
    return x * x


# 一个list
L = list(range(10))
print(L)  # 0-9
print(isinstance(L, Iterable))  # True  list is Iterable
print(isinstance(L, Iterator))  # False

print(range(10))
print(isinstance(range(10), Iterable))  # True range is Iterable
print(isinstance(range(10), Iterator))  # False

r = map(pingfang, L)
print(r)  # <map object at 0x104e23358>
print(isinstance(r, Iterable))  # True
print(isinstance(r, Iterator))  # True

print(list(r))

r = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r)


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def add(a, b):
    return a + b


print(reduce(add, [1, 2, 3, 4, 5, 6]))


def f1(a, b):
    return a * 10 + b


print(reduce(f1, [1, 2, 3, 4, 5, 6]))


def char2int(char):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[char]


print(char2int('1'))
# print(char2int('a'))  # keyError


print(reduce(f1, map(char2int, '13456')))

# 使用lambda进一步简化

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("134523464"))

