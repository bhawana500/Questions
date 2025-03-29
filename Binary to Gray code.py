n=input("enter a binary code: ")
gray=''
k=0
for i in n:
    m=k^int(i)
    gray=gray+str(m)
    k=int(i)
print(gray)
    
    