#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

'''
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
'''

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
def main():
    print('-' * 10)
    with open(r'cookbook/somefile.txt',mode='r') as somefile:
        for line, preLines in search(somefile, 'Python', 3):
            for pline in preLines:
                print(pline)
            print(line)
            print('-' * 10)

if __name__ == '__main__':
    main()