#!/usr/bin/env python3
# encoding: utf-8
"""
@file: hello.py
@user: muyi-macpro
@time: 2018/4/16 下午11:03
@desc: 
"""


def application(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

