# encoding: utf-8
"""
@file: Generator.py
@user: muyi-macpro
@time: 2018/4/1 下午9:34
@desc: python高级特性——生成器
"""

# 第一种方法：把[] 改为 ()

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而G是一个generator。
L = [x * x for x in range(1, 11)]
print(L)

G = (x * x for x in range(1, 11))  # 类似于一个状态机
print(G)

print(next(G))
print(list(G))
# print(next(G))  # StopIteration

G = (x * x for x in range(1, 11))  # 类似于一个状态机
for g in G:
    print(g)


# 通过定义函数的方式创建generator
def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(6))
print(list(fib(6)))

g = fib(6)
while True:
    try:
        x = next(g)  # 注意：每次fib(6)执行得到一个新的generator
        print('g:', x)
    except StopIteration as e:  # 通过catch stopIteration异常来获得函数执行结束的return值
        print('Generator return value:', e.value)
        break
