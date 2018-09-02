# encoding: utf-8
"""
@file: Filter.py
@user: muyi-macpro
@time: 2018/4/2 下午11:42
@desc: filter()
"""


# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, range(10))))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ["sgewrg", None, "gwg", "", "   "])))

# 用filter求素数


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


# 这里是返回了一个函数，
# 作用是 给定一个n生成一个函数，这个函数用来判断传入的x是不是n的倍数
# 相当于下面写法：
def _not_divisible_(n):
    def f(x):
        return x % n > 0
    return f


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield
        # 下面的意思是：对于序列的第一个数，依次判断序列中所有数是不是它的倍数，并过滤掉倍数
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break






