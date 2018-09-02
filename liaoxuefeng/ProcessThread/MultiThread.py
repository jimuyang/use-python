#!/usr/bin/env python3
# encoding: utf-8
"""
@file: MultiThread.py
@user: muyi-macpro
@time: 2018/4/10 下午11:11
@desc: 
"""

if __name__ == '__main__':
    import time, threading

    # 新线程执行的代码:
    def loop():
        print('thread %s is running...' % threading.current_thread().name)
        n = 0
        while n < 5:
            n = n + 1
            print('thread %s >>> %s' % (threading.current_thread().name, n))
            time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)


    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
    pass
