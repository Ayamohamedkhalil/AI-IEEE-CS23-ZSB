import math
def median(lst):
    lst.sort()
    if len(lst)%2==0 :
        num1=lst[len(lst)//2]
        num2=lst[len(lst)//2 - 1]
        median=(num1+num2)/2
    else:
        median=lst[len(lst)//2]
    return median
def variance(lst):
    mean=sum(lst)/len(lst)
    summation=0
    for i in range (len(lst)):
        summation+=(lst[i]-mean)**2
    return summation/len(lst)
        

def sd(lst):
      return math.sqrt(variance(lst))




lst=[]
lst=list(map(int,input().split()))

print("Min :",min(lst))
#print("Q1 :",)
print("Q2 :",median(lst))
#print("Q3 :",)
print("Max : ",max(lst))
print("Range :",max(lst)-min(lst))
print("Variance :",variance(lst))
print ("Standard Deviation :",sd(lst))