#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 如何调整字符串中文本的格式

import re
print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<date>\d{2})', r'\g<month>/\g<date>/\g<year>', '2019-02-08'))
