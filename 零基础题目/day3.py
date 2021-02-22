# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:30:56 2021
编写一个函数，返回所输入的字符串中，具有重复的字符串的数量

@author: yaodan
"""
import time
start =time.clock()

def duplicte_count(text):
    text = str.upper(text) #不区分大小写，所以将字符串改写成全大写
    a1 = len(text) #获取字符串的长度
    count1 = 0 #定义重复字符串的数量
    text_dup = '' #定义重复字符串库
    for numbers in range(a1): #从每个字符开始统计是否重复
        if text[numbers] in text_dup: #若这个字符已经在重复字符库内，则跳过此次循环
            continue
        for  numbers1 in range(numbers+1,a1): #若这个字符不在重复字符库内，则搜寻是否有重复的字符
            if text[numbers1] == text[numbers]:
                count1 += 1
                text_dup += text[numbers]
                break #找到一个与之重复的字符后，更新重复库，加一重复数的标志位，即退出此次循环，不再搜寻
    return count1
                
                
print(duplicte_count('abcde'))
print(duplicte_count('aabBcde'))
print(duplicte_count('indivisibility'))

end = time.clock()
print('Running time: %s Seconds'%(end-start))