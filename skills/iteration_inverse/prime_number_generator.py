#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 一个素数的生成器


class PrimeNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 判断一个数字是否是素数 
    def is_prime_number(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.is_prime_number(k):
                yield k

def main():
    for x in PrimeNumbers(0, 100):
        print(x)

if __name__ == '__main__':
    main()