# -*- coding=UTF-8 -*-
"""
this module is most important in this system
to create a timer for teacher who enter the list
do the calculation by the timer
"""

import time
import re
import threading
from __init__ import readini
from manage_checkindata import ResultManager


class Timer(object):
    """
    do the exactly timer
    """

    def __init__(self):
        """
        do the initialize
        """
        self.timer = None
        self.manager = ResultManager()

    def time_check(self):
        """
         do the main work for timer
         to do the time calculation if two teacher enter the list on the same time
        :return:
        """
        if readini.List == []:
            print "the queue is empty!"
            return
        else:
            line = readini.List[0]
            self.manager.manage_action(line[0], line[1])
            print "即将提出上一位教师"
            readini.List.pop(0)
            self.stop_checkin()

    # 教师进入队列后开始进行倒计时
    def start_checktime(self):
        """
         start the timer
        :return:
        """
        self.timer = threading.Timer(100, self.time_check)
        self.timer.start()

    def stop_checkin(self):
        """
        do the calculation
        :return:
        """
        if self.timer != None:
            if readini.List != []:
                line = readini.List[0]
                self.manager.manage_action(line[0], line[1])
                read = readini()
                clist = read.List
                # leaveTime = clist[0]
                # leaveTimeArray = leaveTime.split('-| | :')
                # print leaveTime
                # print leaveTimeArray
                begin_time = clist[0][3]
                begin_time_array = re.split('[- :]', begin_time)

                # print beginTimeArray# 3 4 5 为时分秒

                nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
                stime0 = nowtime.split(" ")
                stime1 = stime0[1].split(':')
                hourdev = int(stime1[0]) - int(begin_time_array[3])
                minutedev = int(stime1[1]) - int(begin_time_array[4])
                seconddev = int(stime1[2]) - int(begin_time_array[5])
                # print hourdev
                # print minutedev
                # print seconddev

                # 用第二位教师的开启时间和现有时间作对比dev=（100-（nowtime-t2starttime））
                # 目的是计算第二位教师的考勤剩余时间，并赋给计时器
                timedevbuffer = abs(hourdev) * 3600 + minutedev * 60 + seconddev
                timedev = 100 - timedevbuffer
                print '队首教师剩余时间为', ":", timedev
                if timedev < 0:
                    return
                readini.List.pop(0)  # 计算后将教师踢出队列
                # 先取消上次计时后，再传入新的计时值
                self.timer.cancel()
                self.timer = threading.Timer(timedev, self.time_check)
                self.timer.start()
            else:
                print '当前队列已经没有教师'
                return
        else:
            self.timer = threading.Timer(100, self.time_check)
            self.timer.start()


if __name__ == '__main__':
    pass
