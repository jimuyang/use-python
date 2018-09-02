#!/usr/bin/env python3
# encoding: utf-8
"""
@file: network.py
@user: muyi-macpro
@time: 2018/4/12 下午11:27
@desc: 
"""
# 网络通信就是两个进程的通信


if __name__ == '__main__':
    # 导入socket库:
    import socket

    # 创建一个socket:
    # 创建Socket时，AF_INET指定使用IPv4协议
    # SOCK_STREAM指定使用面向流的TCP协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('www.sina.com.cn', 80))

    # 发送数据:
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)

    # 关闭连接:
    s.close()

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('../../resource/sina.html', 'wb') as f:
        f.write(html)

    pass
