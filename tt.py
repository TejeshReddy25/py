n=int(input())
a=bin(n)
print(a)
for i in range(2,len(a)):
    if str(i)==0:
        a.replace('0','1')
    else:
        a.replace('1','0')
print(a)
    
    
    

