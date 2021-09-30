#list of prime
n=int(input())
for i in range(2,n+1):
    for j in range(2,n+1):
        if i%j!=0:
            print(i)
            break
        else:
            break
        
        
            
    
#list of prime vamsi

def prime(inp):
   
    for i in range(2,inp):
        if inp%i==0:
            return False
            break 
        else:
            return True
            break

n=int(input())
a=[]
for i in range(2,n+1):
    if prime(i):
        a.append(i)
print(a)

   
        
