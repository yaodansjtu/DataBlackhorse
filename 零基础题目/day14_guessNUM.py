# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:05:07 2021

@author: yaodan
"""

import re
import random
from pprint import pprint

res1 = random.randint(1,100)
N = 0
while (True):
    num1 = input('请猜一个数字，范围1~100：')
    if len(re.findall(r'\D',num1)) >0:
        pprint('输入错误，请重新输入')
    else:
        num1 = int(num1)
        N += 1
        if num1 == res1:
            pprint('恭喜你，猜中了！共猜了'+str(N)+'次')
            break
        elif num1 >res1:
            pprint('太大了，请重新输入')
        elif num1 <res1:
            pprint('太小了，请重新输入')
