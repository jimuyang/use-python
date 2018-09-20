#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# string trim

str1 = '  nick2008@gmail.com  '
str2 = 'hello world \r\n'

print(str1[0])

print(str1.strip())

str3 = '----sffewf ++ -- s43g +++'
print('(' + str3.strip('-+') + ')')

str4 = 'abc:135'
print(str4[:3] + str4[4:])
print(str4.replace(':', ''))

str5 = 'sfsd: tgt , g'
import re
print(re.sub(r'[:\s,]', '', str5))

str6 = 'abc1345413xyz'

import unicodedata

def make_trans_table(source, target):
    table = {}
    tl = len(target)
    for i in range(len(source)):
        # print(type(source[i]))
        if i < tl:
            # 不超过target长度可以从target取值
            table[ord(source[i])] = ord(target[i])
        else:
            table[ord(source[i])] = None
    return table

# trans_table = str.maketrans('abcxyz', 'xyzabc')
trans_table = make_trans_table('abcxyz4', 'xyzabc')
print(trans_table)

# 
print(str6.translate(trans_table))
