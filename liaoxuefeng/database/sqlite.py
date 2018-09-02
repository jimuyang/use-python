#!/usr/bin/env python3
# encoding: utf-8
"""
@file: sqlite.py
@user: muyi-macpro
@time: 2018/4/15 下午11:21
@desc: 
"""

# 导入SQLite驱动:
import sqlite3


def create():
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
    # <sqlite3.Cursor object at 0x10f8aa260>
    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michael\')')
    # <sqlite3.Cursor object at 0x10f8aa260>
    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)
    # 1
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()


def query():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('SELECT * FROM user WHERE id=?', ('1',))
    # <sqlite3.Cursor object at 0x10f8aa340>
    # 获得查询结果集:
    values = cursor.fetchall()
    print(values)
    # [('1', 'Michael')]
    cursor.close()
    conn.close()


# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

if __name__ == "__main__":
    query()
