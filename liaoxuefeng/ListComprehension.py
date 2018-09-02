# encoding: utf-8
"""
@file: ListComprehension.py
@user: muyi-macpro
@time: 2018/4/1 下午2:52
@desc: python高级特性——列表生成器
"""
import os

# 生成1-10
print(list(range(1, 11)))
print([x for x in range(1, 11)])

# 生成 1*1 - 10*10
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

# 生成全排列
print([m + n for m in 'abc' for n in '123'])

# 列出本列表下所有文件
print([d for d in os.listdir('.')])
