#!/usr/bin/env python3
# encoding: utf-8
"""
@file: MetaClazz.py
@user: muyi-macpro
@time: 2018/4/6 下午4:46
@desc: 
"""


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


# metaclass
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

# 类是metaclass创建的'实例'


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    # mcs:当前准备的创建的类
    # name:类的名字
    # bases:类的父类集合
    # namespace:类的方法集合
    def __new__(mcs, name, bases, namespace):
        namespace['add'] = lambda self, value: self.append(value)
        return type.__new__(mcs, name, bases, namespace)


# 当我们传入关键字参数metaclass时，魔术就生效了，
# 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
class MyList(list, metaclass=ListMetaclass):
    pass


if __name__ == '__main__':
    # <class 'type'>
    # <class '__main__.Hello'>
    print(type(Hello))  # Hello是一个类，它的type是type
    print(type(Hello()))  # Hello() 是一个实例，它的type是Hello这个class

    # 因此，可以通过class创建实例，也可以通过type()创建class

    def fn(self, name='world'):  # 先定义函数
        print('Hello, %s.' % name)


    Hello2 = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
    h = Hello2()

    print(h)
    print(Hello2)
    h.hello()

    # 要创建一个class对象，type()函数依次传入3个参数：
    # class的名称；
    # 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    # class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
    # 通过type()函数创建的类和直接写class是完全一样的，
    # 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

    # print(help(type))

    l = MyList()
    l.add(1)
    l.add(2)
    print(l)

