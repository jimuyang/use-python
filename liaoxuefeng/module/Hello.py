# encoding: utf-8
"""
@file: Hello.py
@user: muyi-macpro
@time: 2018/4/6 上午11:43
@desc: 
"""
import sys

# 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '

__author__ = 'Jimu Yang'


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('too many args!')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

if __name__ == '__main__':
    test()
