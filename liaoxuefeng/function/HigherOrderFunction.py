# encoding: utf-8
"""
@file: HigherOrderFunction.py
@user: muyi-macpro
@time: 2018/4/2 下午11:14
@desc: 高阶函数
"""

# 函数名其实就是指向函数的变量
fun = abs
print(fun(-14))

# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，
# 这种函数就称之为高阶函数。


def add(a, b, func):
    return func(a) + func(b)


print(add(-1, -2, abs))

