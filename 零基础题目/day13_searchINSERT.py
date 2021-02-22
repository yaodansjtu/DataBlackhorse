# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:12:08 2021

求待插入的位置，给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。（说明：数组中无重复元素）

@author: yaodan
"""


def searchInsert(nums: [int], target: int) ->int:
    L = 0
    R = len(nums)-1
    target_index = -1 #把找到或返回的位置初始化为-1
    if target == nums[R]: #先列出几种特殊情况
        target_index = R
    elif target > nums[R]:
        target_index = R+1
    elif target <= nums[L]:
        target_index = 0
    while R-L>1: #当nums[0] < target < nums[R]时，进行二分查找
        mid = (L+R)//2
        if nums[mid] == target:
            target_index = mid
            break
        elif nums[mid] > target:
            R = mid
        else:
            L = mid
    if target_index == -1: #如果二分法没能找到目标值，则将其插入原R（或L+1）的位置
        target_index = R
   
    return target_index

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))
print(searchInsert([1,3,5,6],0))