num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
l=[num1,num2,num3]
print("All possible combinatons of three numbers are: ")
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i==j or j==k or k==i:
                pass
            else:
                print(l[i],l[j],l[k],sep="")
                
                