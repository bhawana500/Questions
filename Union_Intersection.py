l1=[1,2,3,4,56,6,2]
l2=[4,2,98,5,7,8,9,3,5,6,2,1,53,8,2,2]
union=set(l1+l2)
intersection=[]
for i in l1:
    for j in l2:
        if i==j:
            intersection.append(i)
intersection=set(intersection)
print('union=',union)
print("intersection=",intersection)
        