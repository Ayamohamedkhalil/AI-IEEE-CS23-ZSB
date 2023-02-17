def mean(lst):
    return sum(lst)/len(lst)
def median(lst):
    lst.sort()
    if len(lst)%2==0 :
        num1=lst[len(lst)//2]
        num2=lst[len(lst)//2 - 1]
        median=(num1+num2)/2
    else:
        median=lst[len(lst)//2]
    return median    

def mode(lst):
    return max(set(lst),key=lst.count)

lst=[]
lst=list(map(int,input().split()))
print("Mean : ",mean(lst))
print("Median :",median(lst))
print("Mode :",mode(lst))
#print(5//2)
