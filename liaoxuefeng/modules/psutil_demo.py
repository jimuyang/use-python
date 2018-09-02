#!/usr/bin/env python3
# encoding: utf-8
"""
@file: psutil_demo.py
@user: muyi-macpro
@time: 2018/4/13 上午2:08
@desc: 
"""
import psutil

if __name__ == '__main__':
    print(psutil.cpu_count())

    print(psutil.cpu_count(logical=False))

    print(psutil.virtual_memory())

    print(psutil.swap_memory())

    pass
