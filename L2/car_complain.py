# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:05:51 2021

@author: yaodan
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

#投诉编号	投诉品牌	投诉车系	投诉车型	问题简述	典型问题	投诉时间	投诉状态
result1 = pd.DataFrame(columns = ['id','brand','car type','detail type','description','problem type','date','status'])

def get_html(url):
    
    # 得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(url,headers=headers,timeout=10)
    content = html.text
    return content

def analysis(content):
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    df = pd.DataFrame(columns = ['id','brand','car type','detail type','description','problem type','date','status'])
    temp = soup.find('div',class_='tslb_b')
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        dic = {}
        if len(td_list)>0:
            dic = {'id':td_list[0].text,'brand':td_list[1].text,'car type':td_list[2].text, \
                   'detail type':td_list[3].text,'description':td_list[4].text,'problem type':td_list[5].text, \
                    'date':td_list[6].text,'status':td_list[7].text}
            df = df.append(dic, ignore_index = True)
    return df
#爬取20页的抱怨
for i in range(20):
    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-' + str(i+1) + '.shtml'
    content1 = get_html(url)
    df1 = analysis(content1)
    result1 = result1.append(df1, ignore_index = True)
    
print(result1)
result1.to_csv('car_complain.csv',index = False)
result1.to_excel('car_complain.xlsx',index = False)