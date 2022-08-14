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
from time import sleep


class Uart(object):
    def __init__(self, port, baud):
        self.err = 0
        try:
            self.serial = serial.Serial(port, baud)
            print("打开串口成功")
        except:
            print("打开串口失败")
            self.err = -1

    def uar_recv_thread(self):
        print("运行uart_recv_thread")
        while (True):
            try:
                recv_data_raw = self.serial.readline()
                data = "接收----PC" + recv_data_raw.decode()
                print(data)
            except:
                print("接收数据错误!")
                break

    def start_recv_thread(self):  # 接收线程
        thread = threading.Thread(target=self.uar_recv_thread(), daemon=True)
        thread.start()

    def send_uart_data(self, data):  # 发送数据
        self.serial.write(data.encode())

    def uart_close(self):  # 关闭端口
        self.serial.close()


if __name__ == '__main__':
    myuart = Uart("com2", 9600)
    if (0 == myuart.err):
        print("打开串口成功")
        # 如果打开串口成功,启动接收线程,准备实时的接收数据
    myuart.start_recv_thread()
    while (True):
        input_data = input("输入要发送的数据...")
        if (input_data == "quit"):
            # 退出
            myuart.uart_close()
            break
        else:
            # 发送数据给设备
            myuart.send_uart_data(str(input_data))
        sleep(0.01)
    print("退出")
