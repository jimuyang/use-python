#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

p = (4, 5)
x, y = p

print(x, y)

data = ['AVMC', 50, 9.1, (2023, 14, 52)]
name, shares, price, date = data

print(name, shares, price, date)

year, month, day = date
print(year, month, day)

# 解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
# 包括字符串，文件对象，迭代器和生成器。

# 这里必须用5个变量进行解压
string = 'hello'
a, b, _, d, _ = string
print(a, b, d)

# 介绍星号表达式的作用
# from functools import reduce

def average(nums):
    return sum(nums) / len(nums)

def average_drop_first_last(grades):
    grades = sorted(grades)
    _, *middle, _ = grades
    return average(middle)


# 每条记录包括一个name email和不定数量的电话号码
record = ('Dave', 'dave@example.com', '773-31245-3245', '3145-234-3215')
name, email, *phone_numbers = record
print(name, email, phone_numbers[0])




from random import randint
def main():
    grades = [randint(60, 100) for _ in range(20)]
    print('average grade is %s' % average_drop_first_last(grades))

if __name__ == '__main__':
    main()

