def sod(n):
    if len(str(n))==2:
        return n//10+n%10
    elif len(str(n))==1:
        return n
    else:
        return n%10+sod(n//10)
print(sod(153))
        
