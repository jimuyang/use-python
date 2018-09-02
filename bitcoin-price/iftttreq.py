#!/usr/bin/env python3
# encoding: utf-8
"""
@file: iftttreq.py
@user: muyi-macpro
@time: 2018/4/22 下午3:57
@desc: 
"""

import requests
# Make sure that your key is in the URL
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/cDQZ4TFRsZQgpXimWgXJ75'
requests.post(ifttt_webhook_url)

