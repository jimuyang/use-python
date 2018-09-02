#!/usr/bin/env python3
# encoding: utf-8
"""
@file: main.py
@user: muyi-macpro
@time: 2018/4/22 下午3:24
@desc: 
"""

import requests

bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

response = requests.get(bitcoin_api_url)
response_json = response.json()

print(type(response_json))

# Bitcoin data is the first element of the list

print(response_json[0])

