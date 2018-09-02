#!/usr/bin/env python3
# encoding: utf-8
"""
@file: GetClazzInfo.py
@user: muyi-macpro
@time: 2018/4/6 下午12:22
@desc: 
"""
import types

# use type()


if __name__ == '__main__':
    print(type(134))
    print(type('str'))
    print(type(None))
    print(type(abs))

    print(type(1435) == int)
    print(type('str') == str)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)

    print(isinstance(b'a', bytes))

    print(dir('abc'))

    # 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
    # 在Python中，如果你调用len()函数试图获取一个对象的长度，
    # 实际上，在len()函数内部，它自动去调用该对象的__len__()方法

    # 仅仅把属性和方法列出来是不够的，
    # 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

    pass
