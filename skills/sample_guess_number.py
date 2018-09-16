#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

from collections import deque
from random import randint
history = deque([], 5)

# 简单的猜数字游戏
def main():
    while(True):
        guessed = input('Please enter a number to guess: ')
        if guessed.isdigit():
            i = int(guessed)
            history.append(i)
            if guess(i):
                break
        elif guessed == 'history' or guessed == 'h?':
            print(history)

N = randint(0, 99) 
def guess(k):
    if k == N:
        print('Right!')
        return True
    if k < N:
        print('%s is less than N' % k)
    else:
        print('%s is greater than N' % k)
    return False

if __name__ == '__main__':
    main()