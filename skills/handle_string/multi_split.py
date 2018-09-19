#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 使用多种分割符分割字符串

string = '1,34,64rw,;we,tv\tyb;ti|314'

res = string.split(',')
print(res)

# def string_split(str):
#     temp_list.extend(str.split(';'))

temp_list = []
list(map(lambda x: temp_list.extend(x.split(';')), res))
print(temp_list)
res = temp_list

temp_list = []
list(map(lambda x: temp_list.extend(x.split('\t')), res))
print(temp_list)
res = temp_list

temp_list = []
list(map(lambda x: temp_list.extend(x.split('|')), res))
print(temp_list)
res = temp_list

def mysplit(string, ds):
    res = [string]

    for d in ds:
        temp_list = []
        list(map(lambda x: temp_list.extend(x.split(d)), res))
        res = temp_list
    return [x for x in res if x]

print('-----')
print(mysplit(string, ',;\t|'))

# 使用re
print('-----')
import re
print(re.split(r'[,;\t|]+', string))