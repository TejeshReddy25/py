#fibanocci
n=int(input("enter the number upto what number u want to print fibanocci"))
a=0
b=1
sum=0
count=1
while count<=n:
    print(sum)
    count+=1
    a=b
    b=sum
    sum=a+b
