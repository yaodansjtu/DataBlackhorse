# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:04:53 2021

Day16,查找股票，使用列表解析式/生成器表达式
1）用到价格大于150元的股票构造一个新的字典
即 {'MSFT': 165.51, 'FB': 174.79, 'IBM': 121.15, 'GOOG': 1210.41}
2）将key与value对调
即 {165.51: 'MSFT', 174.79: 'FB', 19.63: 'YHOO', 121.15: 'IBM', 1210.41: 'GOOG'}

@author: yaodan
"""
dic = {'MSFT':165.51,'FB':174.79,'YHOO':19.63,'IBM':121.15,'GOOG':1210.41}
dic1 = {keys: values for keys,values in dic.items() if values > 150}
dic2 = {values: keys for keys,values in dic.items()}
print(dic1)
print(dic2)

#print(dic.items())