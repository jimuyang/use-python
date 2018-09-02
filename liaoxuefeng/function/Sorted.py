# encoding: utf-8
"""
@file: Sorted.py
@user: muyi-macpro
@time: 2018/4/2 下午11:53
@desc: 
"""

print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 忽略大小进行排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
