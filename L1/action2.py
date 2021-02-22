# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:55:34 2021

@author: yaodan
"""

#使用numpy创建结构数组

import numpy as np1
persontype = np1.dtype({'names':['name','chinese','maths','english','total_score'],'formats':['S32','i','i','i','i']}) #PPT讲义中的‘f’是什么意思?
people = np1.array([('zhang fei',68,65,30,0),('guan yu',95,76,98,0),('liu bei',98,86,88,0),('dian wei',90,88,77,0),('xu zhu',80,90,90,0)],dtype = persontype)
#print(people)

#将各科分数提取出来
chineses = people['chinese']
mathss = people['maths']
englishs = people['english']
score = people['total_score']
#print(chineses)

print('语文：')
print('平均成绩：',np1.mean(chineses))
print('最小成绩：',np1.min(chineses))
print('最大成绩：',np1.max(chineses))
print('方差：',np1.var(chineses))
print('标准差：',np1.std(chineses),'\n')

print('数学：')
print('平均成绩：',np1.mean(mathss))
print('最小成绩：',np1.min(mathss))
print('最大成绩：',np1.max(mathss))
print('方差：',np1.var(mathss))
print('标准差：',np1.std(mathss),'\n')

print('英语：')
print('平均成绩：',np1.mean(englishs))
print('最小成绩：',np1.min(englishs))
print('最大成绩：',np1.max(englishs))
print('方差：',np1.var(englishs))
print('标准差：',np1.std(englishs),'\n')

#计算总成绩
people['total_score'] = chineses + mathss + englishs  #np1.add函数是否不能用以多个数组相加?
#结构数组可以拓展结构吗？（加入总分）
sort = people['total_score'].argsort() #得到按总分排序的索引号
for number in range(5):
    print("第",number+1,'名：',people[4-number]['name'],people[4-number]['total_score'])
    
    #为什么输出名字会有个b'?
    
    