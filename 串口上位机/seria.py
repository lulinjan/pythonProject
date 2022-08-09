#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time : 2022/8/9
@Author : Administrator
@File : seria
@Description : 
"""

import sys
import serial
import threading


class Uart(object):
    def __init__(self, port, baud):
        self.err = 0
        try:
            self.serial = serial.Serial(port, baud)
            print("打开串口成功")



        except:
            print("打开串口失败")
            self.err = -1


if __name__ == '__main__':
    myuart = Uart("com3", 9600)
    if (0 == myuart.err):
        print("打开串口")
