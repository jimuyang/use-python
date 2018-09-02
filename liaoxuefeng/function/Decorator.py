# encoding: utf-8
"""
@file: Decorator.py
@user: muyi-macpro
@time: 2018/4/3 下午10:59
@desc: 装饰器
"""


def now():
    print('now')


f = now
f()


# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数

# 定义一个打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数
# 把@log放到func()函数的定义处，相当于执行了语句：
# func = log(func)
@log
def func(s):
    print(s)


func('hello')


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
# 自定义文本的log
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-25')


now()

# 函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
print(now.__name__)  # wrapper


# 一个完整的decorator函数写法如下：
import functools


# 不带参数的decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 带参数的decorator
def log(text):
    def decorator(func):
        # 这里 wrapper = functools.wraps(func)(wrapper)
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator






