#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 生成器 generator

def func():
    yield 1
    yield 2
    yield 3

def main():
    g = func()
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    # print(g.__next__())  # StopIteration
    print(g.__iter__() is g)  # True
    # 一个包含yield函数的返回值是一个generator生成器，
    # 它是一个Iterable可迭代对象，它的Iterator是它本身
    

if __name__ == '__main__':
    main()