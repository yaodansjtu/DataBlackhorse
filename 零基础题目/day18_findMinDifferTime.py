# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 09:14:23 2021
最小时间差，
给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示，输入: ["23:59","00:00"]，输出: 1
@author: yaodan
"""

def findMinDifference(timepoints):

    timeMinutes = []
    for time in timepoints:
        time1= time.split(':')
        timeMinutes.append(int(time1[0])*60 + int(time1[1]))
    timeMinutes.sort() #按分钟数排序
    for i in range(len(timeMinutes)):
        timeMinutes.append(timeMinutes[i]+24*60) #加入第二天的时间点
    #print(timeMinutes)
    MinDiff = timeMinutes[1]-timeMinutes[0] #初始化时间差
    for i in range(len(timeMinutes)-1):
        if timeMinutes[i+1]-timeMinutes[i] < MinDiff:
            MinDiff = timeMinutes[i+1]-timeMinutes[i]
    return MinDiff


print(findMinDifference(['23:59','00:00']))
print(findMinDifference(['21:59','00:30','00:05','20:55']))
print(findMinDifference(['23:59','00:30','00:05','20:55']))