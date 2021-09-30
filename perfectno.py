#perfect number
n=int(input("enter the no"))
a=0
for i in range(1,n):
    if n%i==0:
        a=a+i
if a==n:
    print("perfect number")
        
        
