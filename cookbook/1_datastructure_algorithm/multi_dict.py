#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

'''
怎样实现一个键对应多个值得字段
'''

from collections import defaultdict

dd = defaultdict(list)

dd['a'].append(1)
dd['a'].append(2)
dd['a'].append(3)
dd['b'].append(1)
dd['b'].append(2)

print(dd)

