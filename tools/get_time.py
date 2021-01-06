
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time :2020/7/30 0030 15:05
#@Author :dongdong
#@File :get_time.py

import time


def getTime(data):
    timeArray = time.strptime(data, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))*1000
    return timeStamp


#
if __name__ =='__main__':
  getTime('2013-10-10 23:40:00')