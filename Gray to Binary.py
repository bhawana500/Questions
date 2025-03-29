n=input("enter a gray code:")
bin=0
s=''
for i in n:
    i=int(i)
    bin=bin^i
    s=s+str(bin)
print(s)
    
    