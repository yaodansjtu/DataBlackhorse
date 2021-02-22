# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:53:26 2021

@author: yaodan
"""
import time
start =time.clock()


def duplicte_count(text):
    text = text.upper()
    dict = {}
    for i in text:
        if i in dict.keys():
            dict[i] +=1
        else:
            dict[i] = 1
    sum = 0
    for i in dict:
        if dict[i]>1:
            sum = sum +1
    return sum

print(duplicte_count('abcde'))
print(duplicte_count('aabBcde'))
print(duplicte_count('indivisibility'))

end = time.clock()
print('Running time: %s Seconds'%(end-start))