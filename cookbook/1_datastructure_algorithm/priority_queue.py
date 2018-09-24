#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

'''
如何实现一个优先级队列
'''

import heapq

class PriorityQueue:
    
    def __init__(self):
        self._queue = []
        self._index = 0

    def pop(self):
        return heapq.heappop(self._queue)
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

def main():
    pq = PriorityQueue()
    pq.push('hello', 4)
    pq.push('bob', 8)
    pq.push('jim', 9)
    pq.push('grop', 1)

    for _ in range(4):
        print(pq.pop())


if __name__ == '__main__':
    main()
