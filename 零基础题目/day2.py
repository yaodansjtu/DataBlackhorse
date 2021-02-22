# -*- coding: utf-8 -*-
"""
DNA中有4中碱基，分别为ATCG,A和T互补，C和G互补，编写一个函数，输入一个碱基对，输出其互补碱基对
"""


def DNA_strand (str2):
    str1 = ''
    for numbers in range(len(str2)):
        if str2[numbers] == 'A':
            str1 += 'T'
        elif str2[numbers] == 'T':
            str1 += 'A'
        elif str2[numbers] == 'C':
            str1 += 'G'            
        elif str2[numbers] == 'G':
            str1 += 'C'
        else:
            print('输入有误')
    return str1

print(DNA_strand('ATTGC'))
print(DNA_strand('AAAA'))
print(DNA_strand('ATCGT'))


'''
translate函数法
'''

def DNA_strand1 (str2):
    trantab = str.maketrans('ATGC', 'TACG')
    string11 = str2.translate(trantab)
    return string11
print(DNA_strand1('ATTGC'))
print(DNA_strand1('AAAA'))
print(DNA_strand1('ATCGT'))


'''
字典法
'''
dict1 = {'A':'T','T':'A','G':'C','C':'G'}
#例如 dict1['A'] 则得到'T'