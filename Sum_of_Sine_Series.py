term=int(input("Enter the number of terms: "))
x=int(input("Enter the value of x: "))
k=1
s=0
n=1
for m in range(1,term+1):
    if k%2==0:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        s=s-pow(x,n)/fact
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        s=s+pow(x,n)/fact
    n=n+2
    k+=1
print("Sum of sine series=",s)