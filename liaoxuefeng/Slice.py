# encoding: utf-8
"""
@file: Slice.py
@user: muyi-macpro
@time: 2018/4/1 上午12:05
@desc: python的高级特性——切片
"""

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 前三个元素
res = [L[0], L[1], L[2]]  # 笨方法
print(res)

res = L[0:3]
print(res)
print(L[:3])  # 0可以省略
print(L[1:3])

print(L[-1])  # 最后一个元素

# 注意倒数切片 顺序并没有发生改变
print(L[-1:])  # 倒数切片
print(L[-2:])  # 倒数切片

L = list(range(1, 100))  # 1-99 同样也是左闭右开区间
print(L)

print(L[1:10])  # 2-10 切片中的数字代表下标 index 同样也是左闭右开区间 即 L[1] - L[9]

print(L[0:10:2])  # 13579 每两个取一个
print(L[89:])  # 90-99





