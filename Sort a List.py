l=[['c',3],['a',1],['d',4],['b',2]]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i][1]<l[j][1]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)