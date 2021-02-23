# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:27:56 2021

删除重复的元素，从数组里面，删除重复的元素。
重复的数字最多只能出现2次（如果之前已经有2次了，那么之后就不会再出现）比如 nums=[1,1,1,2,2,3]，返回nums=[1,1,2,2,3]

@author: yaodan
"""

def removeDuplicates(nums):
    counterDic = {} #模拟Counter类的字典
    num = [] #返回的数组
    for i in range(len(nums)):
        if nums[i] not in counterDic.keys():
            counterDic[nums[i]] = 1
        else:
            counterDic[nums[i]] += 1
        if counterDic[nums[i]] <=2: #若计数>2则不添加此元素
            num.append(nums[i])
    return num

print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([1,2,2,3,5,2,4,5,3,2,1,5]))
print(removeDuplicates([3,2,2,1]))