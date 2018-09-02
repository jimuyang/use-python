#!/usr/bin/env python3
# encoding: utf-8
"""
@file: send.py
@user: muyi-macpro
@time: 2018/4/14 下午7:01
@desc: 
"""

if __name__ == '__main__':
    from email.mime.text import MIMEText

    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

    # 输入Email地址和口令:
    from_addr = '1191242407@qq.com'
    password = 'ebveaxychcfighia'
    # 输入收件人地址:
    to_addr = '17621660286@163.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'

    import smtplib

    server = smtplib.SMTP(smtp_server, 465)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


    pass
