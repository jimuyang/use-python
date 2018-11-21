#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

import itchat

# 自动登录 使用命令行二维码 不重新扫码
itchat.auto_login(hotReload=True)

itchat.send('Hello, 文件助手', toUserName='filehelper')
