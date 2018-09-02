#!/usr/bin/env python3
# encoding: utf-8
"""
@file: ExceptionError.py
@user: muyi-macpro
@time: 2018/4/7 下午4:35
@desc: 
"""
import logging

if __name__ == '__main__':

    # try
    try:
        print('try...')
        r = 10 / int('2')
        print('result:', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
        logging.exception(e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('END')

    # Python的错误其实也是class，所有的错误类型都继承自BaseException，
    # 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

    # 使用python内置的logging模块进行错误记录

    pass
