#！/usr/bin/env python
#-*-coding:utf-8-*-
#1公司所有的网络设备IP池
#2每30秒循环对池内的所有IP进行测试
#3有错误的返回发出警告

import os,time
import sys

ip_True = open('ip_True.txt','w+')
ip_False = open('ip_False.txt','w+')
IPhosts = [
    #交换机组
    #无线AP组
    #服务器组
    #考勤组
    #其它
    #打印机组
    ]

count_True,count_False = 0,0

for ip in IPhosts:
    return1=os.system('ping -n 1 -w 1 %s'%ip)
    if return1:
        ip_False.write(ip+'\n')
        count_False += 1
    else:
        ip_True.write(ip+'\n')
        count_True += 1

ip_False.write(str(count_False)+'\n')		
ip_True.write(str(count_True)+'\n')

ip_True.close()
ip_False.close()
