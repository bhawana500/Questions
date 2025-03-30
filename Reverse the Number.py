num=int(input("Enter a Number: "))
s=0
print("Number Before Reversing:",num)
while num>0:
    r=num%10
    s=s*10+r
    num=num//10
print("Number after Reversing:",s)