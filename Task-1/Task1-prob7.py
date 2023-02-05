a = []
b = []
n = int(input("enter number of elements: "))
for i in range(0,n):
    num =int(input())
    a.append(num)
num =int(input())
for item in range(n-num, n): 
   b.append(a[item]) 
      
for item in range(0, n - num):  
  b.append(a[item]) 
print(b)
