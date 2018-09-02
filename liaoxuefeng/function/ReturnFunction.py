# encoding: utf-8
"""
@file: ReturnFunction.py
@user: muyi-macpro
@time: 2018/4/3 下午10:37
@desc: 返回函数
"""

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 3, 5)
print(f)
print(f())

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。


def count():
    funcs = []
    for i in range(1, 4):
        def func():
            return i * i
        funcs.append(func)
    return funcs


f1, f2, f3 = count()  # 这里是自动解析
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9

# ! 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# 如果要引用循环变量可以：
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count1()  # 这里是自动解析
print(f1())  # 1
print(f2())  # 4
print(f3())  # 9





