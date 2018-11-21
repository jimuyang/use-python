#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jimu Yang'

import requests
import itchat


# TULING_API_URL = 'http://www.tuling123.com/openapi/api'
TULING_API_URL = 'http://openapi.tuling123.com/openapi/api/v2'


def get_response(msg):
    print('get response calling......')
    data = {
        'reqType': 0,
        'perception':{
            'inputText': {
                'text': msg
            }
        },
        'userInfo': {
            'apiKey': 'bcb7bbb2e577484cba4bdca41669d733',
            'userId': '335036'
        },
    }
    try:
        r = requests.post(TULING_API_URL, data=data).json()
        print('request result: ' + r)
        return r.get('results')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    print(msg.User)
    print((msg.User['RemarkName'] or msg.User['NickName']) + ' : ' + msg['Text'])
    defaultReply = 'I received: ' + msg['Text']
    tuling_reply = 'I am a Robot: ' + get_response(msg['Text'])
    print(tuling_reply)
    return tuling_reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
    