#!/usr/bin/env python3
# encoding: utf-8
"""
@file: server.py
@user: muyi-macpro
@time: 2018/4/16 下午11:03
@desc: 
"""
# 从wsgiref.simple_server 导入
from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 9000, application)
print('Serving HTTP on port 9000...')
# 开始监听HTTP请求:
httpd.serve_forever()
