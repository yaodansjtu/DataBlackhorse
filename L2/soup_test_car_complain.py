# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:41:05 2021

@author: yaodan
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
# 请求URL

def get_page_soup(url_req):
    #得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(url_req,headers=headers,timeout=10)
    content = html.text
    
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

def analysis(soup):
        # 找到完整的投诉信息框
    temp = soup.find('div',class_="tslb_b")
    #投诉编号	投诉品牌	投诉车系	投诉车型	问题简述	典型问题	投诉时间	投诉状态
    keys = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status']
    df = pd.DataFrame(columns = keys)
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) >0:
            temp = {}
            for i,key in enumerate(keys):
                    temp[key] = td_list[i].text
                #优化代码
                
            df = df.append(temp,ignore_index = True)
    return df


base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
result = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])

#循环n页
for i in range(int(input('请输入需要抓取的总页数:'))):
    url = base_url + str(i+1) +'.shtml'
    soup = get_page_soup(url) #得到soup
    df = analysis(soup) #解析得到dafa
    result = result.append(df)
    print('Finish Page:'+str(i))
    time.sleep(0.2)
print(result)


#以下是将problem列的问题代码转化为实际问题名称的代码：

#获取编码和问题对应的字典
soup1 = get_page_soup('http://www.12365auto.com/js/cTypeInfo.js?version=20210303')
import ast
dic1 = str(soup1).strip('var cTypeInfo = ')
dic1 = ast.literal_eval(dic1)

#将编码转换成问题汉字的函数
def get_problemtype(str1):
    type1,type2 = str1[0],int(str1[1:])
    for i in dic1:
        if i['value']==type1:
            for j in i['items']:
                if j['id'] ==type2:
                    return i['name']+'-'+j['title']


for i in range(len(result['problem'])):
    temp1 = result['problem'].values[i].strip(',').split(',') #先去掉句尾的“，”，再拆分
    temp2 = ''
    for str1 in temp1:
        temp2 = temp2 + get_problemtype(str1) +','
    result['problem'].values[i] = temp2

import datetime
time = datetime.datetime.now().__format__('%Y-%m-%d_%H-%M-%S')


result.to_csv('car_complain_'+time+'.csv',index = False)
result.to_excel('car_complain_'+time+'.xlsx',index = False)
