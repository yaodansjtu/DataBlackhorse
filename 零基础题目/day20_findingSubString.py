# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:31:59 2021
ay20：串联所有单词的子串，给定一个字符串 s 和一些长度相同的单词 words。
找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，不需要考虑 words 中单词串联的顺序
输入： s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
@author: yaodan
"""

'''
#这个是把words的元素排列组合，再拿去s里比较的方法
def findSubstring(s, words):
    words = united(words) #递归获取联合起来的word
    words = list(set(words)) #去重
    n1 = len(s)
    n2 = len(words[0])
    index1 = []
    for i in words: #遍历获取s中有没有word
        for j in range(0,n1-n2+1):
            if s[j:j+n2] == i:
                index1.append(j)
    print(index1)
    return index1

def united(words): #递归获取联合起来的word
    if len(words)<=1:
        return words
    else:
        word1 = []
        for i in range(len(words)):
            asd = united(words[:i]+words[i+1:])
            for j in asd:
                word1.append(words[i]+j)
    return word1
'''

#这个是用counter做words元素（定长单词）统计，再分割s做元素统计和对比的方法
def findSubstring(s, words):
    from collections import Counter
    words_hash = Counter(words)
    m = len(words[0])
    n = len(words)
    index1 = []
    for i in range(0,len(s)-m*n+1):
        #temp = s[i,i+m*n]
        s_hash = []
        for j in range(n):
            s_hash.append(s[i+j*m:i+j*m+m])
        s_hash = Counter(s_hash)
        if words_hash == s_hash:
            index1.append(i)
    print(index1)
    return index1
            


findSubstring('barfoothefoobarman',['foo','bar'])
findSubstring('wordgoodgoodgoodbestword',['word','good','best','word'])
findSubstring('wordgoodgoodgoodbestword',['good','best','word'])