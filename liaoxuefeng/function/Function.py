# encoding: utf-8
"""
@file: Function.py.py
@user: muyi-macpro
@time: 2018/3/21 下午11:52
@desc: 
"""

print(abs(-13))

a = 255


def int_to_hex_string(i):
    return str(hex(i))


print(int_to_hex_string(a))

'''
关于函数的参数
1. 必须为不可变对象
2. 

'''


def add_end(L=[]):
    L.append('end')
    return L


print(add_end([1, 2]))
print(add_end([1, 2]))

print(add_end())
print(add_end())


# ['end']
# ['end', 'end']


def add_end(array=None):
    if array is None:
        array = []
    array.append('end')
    return array


print(add_end())
print(add_end())


# 可接收一个或多个数并计算乘积


def product(x, y=1, *others):
    if x is None:
        raise TypeError
    result = x * y
    if len(others) != 0:
        for num in others:
            result = result * num
    return result


# 测试


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

"""
递归函数
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))
print(fact(100))


def fact_tail(n, t=1):
    if n == 1:
        return t
    return fact_tail(n - 1, t * n)


print(fact_tail(10))
# 没有意义 python没有对为递归进行优化
# print(fact_tail(1000))


# 汉诺塔


def move_hannuota(n, a, b, c):
    # 它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
    # 然后打印出把所有盘子从A借助B移动到C的方法，
    if n == 1:
        print(a, '-->', c)
        return
    move_hannuota(n - 1, a, c, b)
    move_hannuota(1, a, b, c)
    move_hannuota(n - 1, b, a, c)


move_hannuota(3, 'A', 'B', 'C')
