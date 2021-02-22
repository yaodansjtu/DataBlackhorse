# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:00:09 2021

@author: hasee
"""
import numpy as np
import pandas as pd

data = pd.read_csv('car_complain.csv')
#data.to_excel('car_complain.xlsx',index = False)


def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
data['brand'] = data['brand'].apply(f)

data = data.drop(['problem'],axis = 1).join(data.problem.str.get_dummies(','))


#按照brand统计投诉的总数
print('\n按照brand统计投诉的总数:')
result = data.groupby(['brand'])['id'].agg(['count'])
#为什么用.agg(['count']) 而不是.count()?
#print(result)
print(result.sort_values(by = ['count'],ascending=False))
#print(result['count'].sum())

#按照车型统计投诉的总数
print('\n按照车型统计投诉的总数:')
result2 = data.groupby(['type'])['id'].agg(['count'])
print(result2.sort_values(by = ['count'],ascending=False))


tags = data.columns[7:]
result3 = data.groupby(['brand'])[tags].sum()
result4 = result.merge(result3,left_index = True, right_index = True, how = 'left')
result4.reset_index(inplace = True)
result4.to_excel('car_complain_set.xlsx',index = False)

#哪个品牌的平均车型投诉最多
print('\n哪个品牌的平均车型投诉最多')
result5 = data.groupby(['brand','type'])['id'].agg(['count'])#将数据按照品牌和车型归类，并计抱怨数
result5 = result5.groupby(['brand'])['count'].mean()#对每个品牌各车型的抱怨数取平均值
print(result5.sort_values(ascending=False))
