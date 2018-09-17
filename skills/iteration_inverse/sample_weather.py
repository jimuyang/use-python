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



# 定义可返回城市天气预报的迭代器对象
class WeatherIterator(Iterator):
    
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    
    def get_weather(self, city):
        resp = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = resp.json()['data']
        # print(data)
        return '%s: %s, %s' % (city, data['forecast'][0]['low'], data['forecast'][0]['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

# 定义可返回城市天气预报的可迭代对象 
class WeatherIterable(Iterable):

    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

def main():
    cities = [u'北京', u'上海', u'南京']
    # print(get_weather(u'北京'))
    for city_weather in WeatherIterable(cities):
        print(city_weather)

if __name__ == '__main__':
    main()