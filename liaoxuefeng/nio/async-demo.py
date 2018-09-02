#!/usr/bin/env python3
# encoding: utf-8
"""
@file: async-demo.py
@user: muyi-macpro
@time: 2018/4/16 下午11:32
@desc: 
"""
import asyncio


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello(), hello()]))
loop.close()
