#armstrong
n=int(input())
m=len(str(n))
temp=n
total=0
while temp>0:
    r=temp%10
    total=total+(r**3)
    temp=temp//10
if total==n:
    print("armstrong")
else:
    print("oops")
    

    
    
    
    
    
