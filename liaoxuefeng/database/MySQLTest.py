#!/usr/bin/env python3
# encoding: utf-8
"""
@file: MySQLTest.py
@user: muyi-macpro
@time: 2018/4/15 下午11:52
@desc: 
"""

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
# 1
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# [('1', 'Michael')]
# 关闭Cursor和Connection:
cursor.close()
conn.close()

if __name__ == '__main__':
    pass
