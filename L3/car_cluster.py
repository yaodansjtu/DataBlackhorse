# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:22:12 2021

@author: yaodan
"""
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

#数据读取和预处理
data = pd.read_csv('car_data.csv', encoding = 'gbk')
print(data)
train_x = data[['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']]
mimmaxscale = preprocessing.MinMaxScaler()
train_x = mimmaxscale.fit_transform(train_x)
print(train_x)
kms = KMeans(n_clusters = 4)
predit_y = kms.fit_predict(train_x)
result = pd.concat((data,pd.DataFrame(predit_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
#result.to_csv("car_cluster_result.csv",index=False)


'''
#kmeams手肘法
import matplotlib.pyplot as plt
sse = []
for k in range(1, 11):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(train_x)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()
'''

#层次聚类

from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

agg = AgglomerativeClustering(linkage='ward',n_clusters = 4)
y = agg.fit_predict(train_x)

linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()
