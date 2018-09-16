#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

# 例子：考试交卷系统模拟


def main():

    from time import time
    from random import randint

    players = list('ABCDEFG')   # 考生们
    start = time()  # 考试开始
    summary = {}

    for x in range(len(players)):
        input()
        p = players.pop(randint(0, len(players)-1))
        print("now the player: %s finish the exam" % p)
        use_time = time() - start
        summary[p] = (x+1, use_time)
    print(summary)


def test():
    from random import randint
    L = [randint(0, 2) for _ in range(10)]
    print(L)    # [0, 2, 1, 1, 1, 2, 0, 0, 1, 2]
    # randint是左右都闭的区间


if __name__ == '__main__':
    # test()
    main()
