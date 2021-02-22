# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:14:57 2021

最长回文子串，寻找输入字符的最长回文子串，
回文代表：正向和反向相等，比如“aba”、“cabbac。
最长回文子串需要满足：1.回文子串；2.该子串是回文子串中长度最长的

@author: yaodan
"""
'''
def longest_plaindrome(s):
    lenth1 = 1 #初始化最长回文子串长度为1
    for i in range(len(s)-1): #思路：判断任意一个子串是否为回文子串
        for j in range(i+1,len(s)):
            if lenth1 < j - i +1:
                s1 = s[i:j+1]
                if s1 == s1[::-1]: #如果反转后与原来相等，则是回文子串
                    lenth1 = j - i +1
    print(lenth1)
'''

def longest_plaindrome(s):
    #manacher算法
    R = -1 #右边界
    C = -1 #得到R时候的i
    lenM = 2*len(s) + 1 #M字符串长度
    lenR = [1,2] #回文半径列表，前两个值位
    #1.预处理得到Manacher字符串
    M = '#'
    for i in range(len(s)):
        M += s[i]
        M += '#'
    #print(M)
    #2.开始算法
    for i in range(2,lenM-1):
        if i>R: #case1,M[i]在之前的回文边界外，遍历，并设定循环结束条件
            l = r =i
            for j in range(lenM): 
                if (l==0 or r==lenM-1):
                    break
                if M[l-1]!=M[r+1]: 
                    break
                l -=1
                r +=1
            if r>R:
                R = r
                C = i
            lenR.append(r-i+1)
        else: #case2,M[i]在之前的回文边界内，再根据L---i'---C---i---R的模型分情况
            L = 2*C - R
            i1= 2*C - i
            if lenR[i1] < i1-L+1:  #如果i'的回文半径在L-R以内，则根据回文子串的对称特性，i的回文半径等于i'
                lenR.append(lenR[i1]) 
            elif lenR[i1] > i1-L+1: #如果i'的回文半径在L-R以外，由于M[L-1]!=M[R+1] (否则之前得不到R),i的回文半径等于i到R
                lenR.append(R-i+1) 
            else: #如果i'的回文半径正好在L上，则需要从R+1，2i-R-1开始做遍历
                r = R
                l = 2*i - R
                for j in range(lenM):
                    if (l==0 or r==lenM-1):
                        break
                    if M[l-1]!=M[r+1]: 
                        break
                    l -=1
                    r +=1
                if r>R:
                    R = r
                    C = i
                lenR.append(r-i+1)
        
    return(max(lenR)-1)
    
    
    
        

longest_plaindrome('a')
longest_plaindrome('aa')
longest_plaindrome('baa')
longest_plaindrome('aab')
longest_plaindrome('abcdefghba')
longest_plaindrome('baablkj12345432133d')