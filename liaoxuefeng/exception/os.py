#!/usr/bin/env python3
# encoding: utf-8
"""
@file: os.py
@user: muyi-macpro
@time: 2018/4/7 下午5:36
@desc: 
"""

if __name__ == '__main__':
    import os
    print(os.name)
    print(os.uname())
    print(os.environ)

    print(os.path.abspath('../..'))

    print(os.path.splitext('/path/to/file.txt'))

    # 当前目录下所有的py文件
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

    pass
