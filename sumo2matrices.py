a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(len(a[0]))
b=[[1,2,3],
   [4,5,6],
   [7,8,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
print(len(a))
print(len(b))
for i in range(len(a)):
  for j in range(len(a[0])):
                 result[i][j]=a[i][j]+b[i][j]
print(result)
