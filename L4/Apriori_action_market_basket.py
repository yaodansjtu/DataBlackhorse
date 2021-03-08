# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:53:25 2021

@author: yaodan
"""
import pandas as pd
import time
import matplotlib.pyplot as plt

data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)

#print(data.shape)

data1=[]#将每一行的数据放在一个列表中，方便处理
data2=[]#将每一行的数据放在str中，方便get_dummies
for i in range(7501):
    data11=[]
    data22=''
    for j in range(20):
        if type(data[j][i])==float or j==19: #只有nan是float，不然就是str
            data1.append(data11)
            data2.append(data22)
            break
        else:
            data11.append(data[j][i])
            data22+=data[j][i]+'/'


def rule1():
    start = time.time()
    from efficient_apriori import apriori
    itemsets, rules = apriori(data1, min_support=0.05,  min_confidence=0.4)
    print("频繁项集：", itemsets)
    print("关联规则：", rules)
    end = time.time()
    print("用时：", end-start)


def rule2():
    start = time.time()
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules
    data_df = pd.DataFrame(data2)
    data_df.columns=['items']
    data2_hot_encoded = data_df.drop('items',1).join(data_df['items'].str.get_dummies('/'))
    frequent_itemsets = apriori( data2_hot_encoded, min_support = 0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.1)
    print("频繁项集：", frequent_itemsets)
    print("关联规则：", rules[ (rules['lift'] >= 1.1) & (rules['confidence'] >= 0.2) ])
    end = time.time()
    print("用时：", end-start)
    
    plt.bar([list(i)[0] for i in frequent_itemsets['itemsets']],frequent_itemsets['support'])
    
rule2()
