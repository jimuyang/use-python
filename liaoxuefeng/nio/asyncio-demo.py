#!/usr/bin/env python3
# encoding: utf-8
"""
@file: asyncio-demo.py
@user: muyi-macpro
@time: 2018/4/16 下午11:29
@desc: 
"""

import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
