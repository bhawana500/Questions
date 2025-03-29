l=[5,7,3,8,3,9,4,1,3,7,9,6,4]
for n in range(1,len(l)):
    check=l[0]
    for i in range(1,len(l)):
        if check>l[i]:
            temp=l[i]
            l[i]=l[i-1]
            l[i-1]=temp
        check=l[i]
s=list(set(l))
print(s[-2])