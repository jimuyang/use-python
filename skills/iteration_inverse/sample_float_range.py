#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 连续浮点数生成器 可反向生成

L = [1, 2, 3, 4, 5]
print(iter(L))
print(reversed(L))

for x in reversed(L):
    print(x)

# iter需要实现 __iter__ 方法
# reversed需要实现 __reversed__ 方法

class FloatRange:

    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

def main():
    fr = FloatRange(1, 4, 0.5)
    for x in fr: 
        print(x)

    for x in reversed(fr):
        print(x)

if __name__ == '__main__':
    main()

