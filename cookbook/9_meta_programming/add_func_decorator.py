#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

import time, logging
from functools import wraps

'''
这里是不带参数的装饰器
一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数。
'''

def timethis(func):
    '''
    Decorator func reports the execution time
    '''
    @wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def test_timethis(n):
    '''
    test
    '''
    while(n > 0):
        n -= 1
'''
装饰器等于
test_timethis = timethis(test_timethis)
'''

# 带上参数的装饰器例子

def logged(level, name=None, message=None):
    '''
    log decorator which u can choose the log level and name
    '''
    def decorate(func):
        log_name = name if name else func.__module__
        logger = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kw):
           logger.log(level, log_msg) 
           return func(*args, **kw)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y

'''
此时装饰器相当于：
add = logged(logging.DEBUG)(add)
'''

@logged(logging.CRITICAL, 'example')
def spam():
    print('spam')


def main():
    test_timethis(10000)

    print(test_timethis.__name__)
    print(test_timethis.__doc__)
    print(test_timethis.__annotations__)
    print(test_timethis.__wrapped__)

    add(1, 4)
    spam()
    

if __name__ == '__main__':
    main()

