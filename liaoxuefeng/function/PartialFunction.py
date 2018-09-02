# encoding: utf-8
"""
@file: PartialFunction.py
@user: muyi-macpro
@time: 2018/4/3 下午11:26
@desc: 偏函数
"""
import functools

print(int('1345'))

print(int('11', base=8))  # 9
print(int('11', base=2))   # 3
print(int('11', base=10))  # 11

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# 这里传入了关键字参数 kw = { 'base': 2 }
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1000000', base=10))

