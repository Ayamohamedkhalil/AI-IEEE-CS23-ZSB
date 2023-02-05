a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input())
    a.append(b)
a.sort()
print(a[n-2],a[1])

