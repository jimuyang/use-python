#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 读写csv文件

import requests
import csv
url = 'http://table.finance.yahoo.com/table.csv?s=000001.sz'
req = requests.get(url)

with open('pinan.csv', 'w') as file:
    file.write(req.content)