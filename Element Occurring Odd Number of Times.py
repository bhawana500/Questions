l=[1,3,2,3,2,1,2,3,2,1,2,3,2,1,3,3,1,3]
s=set(l)
for i in s:
    count=0
    for j in l:
        if j==i:
            count+=1
    if count%2!=0:
        print(f"{i} occurs odd number of times is {count}")