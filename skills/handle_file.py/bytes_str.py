#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 
str1 = '你好'
str2 = '你好'

print(str1.encode('utf-8'))

bytes = str1.encode('utf-8')
for b in bytes:
    print(bin(b))

'''
0b11100100
0b10111101
0b10100000
0b11100101
0b10100101
0b10111101
'''

# print(str2)