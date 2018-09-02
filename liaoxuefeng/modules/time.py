#!/usr/bin/env python3
# encoding: utf-8
"""
@file: time.py
@user: muyi-macpro
@time: 2018/4/11 下午11:26
@desc: 
"""
from datetime import datetime
now = datetime.now()

print(now)
print(now.timestamp())

# string to datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

print(now.strftime('%a, %b %d %H:%M'))

