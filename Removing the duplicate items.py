l=[3,1,2,4,5,1,3,4,5,2,1,3,5,2]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            l[i]='k'
new_list=[]
for i in l:
    if i!='k':
        new_list.append(i)
print(new_list)