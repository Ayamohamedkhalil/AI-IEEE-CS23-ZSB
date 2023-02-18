"""def sort_fun(value):
    for i in range(len(value)):
       for j in range(i , len(lst)-i-1):

            if lst[i] > lst[j]:
                t=lst[i]
                lst[i]=lst[j]
                lst[j]=t"""
def sort_fun(value):
    
    
    value.sort()                
def target_fun(value,target):
    sort_fun(value)
    arr = []
    
    for i in range(len(value)):
        if(value[i] == target):
            arr.append(i)
    print(min(arr),max(arr)) 
                
 
try :   
 value = list(map(int,input().split(",")))
except :
 target = int(input())
 target_fun(value,target)


