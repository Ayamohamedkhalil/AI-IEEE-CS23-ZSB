import numpy as np
arr1=np.diag([9,9,9])
print(arr1,'\n')

#*********************************
arr2 = np.arange(2, 33, 2).reshape(4, 4)
mean = np.mean(arr2)
std = np.std(arr2)
t = (arr2 > (mean - 0.5*std)) & (arr2 < (mean + 0.5*std))
arr2[t]
print( arr2[t],'\n')
#*******************************
arr3 = np.zeros((9, 9), dtype=int)
print(arr3,'\n')
#******************************
n=int(input("Enter The Numbers :"))
length = np.arange(1, n+ 1, dtype = int)
ar1 = np.ones([n,n], dtype = int)
ar2 = length * ar1
print(ar2,'\n')
