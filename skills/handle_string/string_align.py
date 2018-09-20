#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 对字符串进行左、右、居中对齐
# 1：str.ljust() str.rjust() str.center()
# 2: format() 传入：'<20' '>20' '^20'

str1 = 'abcde'

print(str1.ljust(10, '='))
print(str1.rjust(10, '='))
print(str1.center(10, '='))

print(format(str1, '>20'))
print(str1.__format__('^20'))
