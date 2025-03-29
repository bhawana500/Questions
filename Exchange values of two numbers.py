# Exchanging the values without using temporary values
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print(f"Before Exchanging num1={num1} and num2={num2}")
num1=num1+num2  
num2=num1-num2
num1=num1-num2
print(f"After Exchanging num1={num1} and num2={num2}")
