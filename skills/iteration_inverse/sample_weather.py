#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 实现天气的可迭代对象和迭代器对象
from collections import Iterable, Iterator
import requests

print(Iterable.__abstractmethods__)  # frozenset({'__iter__'})
print(Iterator.__abstractmethods__)  # frozenset({'__next__'})

def get_weather(city):
    resp = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = resp.json()['data']
    # print(data)
    return '%s: %s, %s' % (city, data['forecast'][0]['low'], data['forecast'][0]['high'])

def main():
    print(get_weather(u'北京'))

if __name__ == '__main__':
    main()

# 定义可返回城市天气预报的迭代器对象
