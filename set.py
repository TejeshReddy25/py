n=int(input())
arr = list(map(int,input().split()))
set = set(arr)
j=0
k=0
for i in set:
    print(i)
    j=j+i
    k=k+1
print(j/k)
