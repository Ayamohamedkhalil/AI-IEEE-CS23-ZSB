# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:47:40 2023

@author: DELL
"""

lst = list(map(int,input().split()))
max_sum=min_sum=0
max_lst=[]
min_lst=[]
for i in range(len(lst)):
    if lst[i]>=0:
        max_lst.append(lst[i])
        max_sum+=int(lst[i])
    else:
        min_lst.append(lst[i])
        min_sum+=int(lst[i])

lst.sort()
if(len(min_lst)<2):
    min_lst.append(lst[1])
    min_sum+=lst[1]
if(len(max_lst)<2):
    max_lst.append(lst[-2])
    max_sum+=lst[-2]
print("{} ({})".format(max_lst,max_sum))
print("{} ({})".format(min_lst,min_sum))