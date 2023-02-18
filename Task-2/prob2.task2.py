# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:45:41 2023

@author: DELL
"""

    
lst=[]
count=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
   even = len(list(filter(lambda a: (a%2 == 0) , lst)))
print(even)