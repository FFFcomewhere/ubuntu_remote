#!/usr/bin/env python
# coding=utf-8
import serial
import time
import threading
import glob

inhead = 'RECV'  # 接收数据头
outhead = 'SEND'  # 发送数据头


class SerialData(threading.Thread):  # 创建threading.Thread的子类SerialData
    def __init__(self):
        threading.Thread.__init__(self)  # 初始化线程

    def open_com(self, port, baud):  # 打开串口
        self.ser = serial.Serial(port, baud, timeout=0.5)
        return self.ser

    def com_isopen(self):  # 判断串口是否打开
        return self.ser.isOpen()

    def send_data(self, data, outhead=outhead):  # 发送数据
        self.ser.write(outhead + data)

    def next(self):  # 接收的数据组
        all_data = ''
        # if inhead == self.ser.read(1) :
        all_data = self.ser.readline()  # 读一行数据
        return all_data

    def close_listen_com(self):  # 关闭串口
        return self.ser.close()


if __name__ == '__main__':
    try:
        rec_data = SerialData()  # 为串口开辟线程
        allport = glob.glob('/dev/ttyACM*')  # 搜索匹配字符 ‘/dev/ttyACM’的设备
        port = allport[0]
        baud = 9600
        openflag = rec_data.open_com(port, baud)  # 打开串口
        if openflag:
            print( 'i open %s at %s successfully!' % (allport[0], baud))

        rec_data.send_data('---I am the data from pc to mcu ,now i am back to pc !:)')  # 发送数据
        while True:
            com_data = rec_data.next()
            if not com_data == '':
                print('Look what i got :%s' % (com_data))
        rec_data.close_listen_com()  # 关闭串口

    except KeyboardInterrupt:
        rec_data.close_listen_com()  # 关闭串口
        if not rec_data.com_isopen():  # 判断串口是否关闭
           print("erro")












