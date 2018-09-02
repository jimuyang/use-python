#!/usr/bin/env python3
# encoding: utf-8
"""
@file: ConsumerProducer.py
@user: muyi-macpro
@time: 2018/4/16 下午11:20
@desc: 
"""


# 消费者
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


# 生产者
def produce(c):
    # 通知consumer启动
    print(c.send(None))
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 通知consumer可以消费n了，并获得了consumer消费的结果
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
