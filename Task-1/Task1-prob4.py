a=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    b=int(input())
    a.append(b)  
b=int(input()) 
for i in range(0,n):
    for j in range(i,n):
        if a[j]+a[i] == b:
            print(i,j)
            
            

        
            
            

