# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:07:09 2021
Day19：汉明距离，汉明距离应用于很多领域。在编码理论中用于错误检测，在信息论中量化字符串之间的差异
汉明距离 = 两个数字对应二进制位不同的位置的个数，给出两个整数 x 和 y，计算它们之间的汉明距离。
比如输入: x = 1, y = 4  输出: 2
@author: yaodan
"""

def hammingDistance(x,y):
    dis1 = str(bin(x^y))
    dis = 0
    for i in dis1:
        if i =='1':
            dis +=1
    print(dis)
    return dis

hammingDistance(1,4)
hammingDistance(20,34)
hammingDistance(55,34)
hammingDistance(78,96)
hammingDistance(1278,196)