# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:59:19 2023

@author: DELL
"""

from prob4.task2 import dictt
z_filter=open("filtered.txt",'w')
for i in dictt.keys():
    z_filter.write("\n{} {}-{}".format(i,dictt[i]['name'],dictt[i]['birthyear']))
z_filter.close()