# Print n+nn+nnn.... till given terms
n=int(input("Enter number n: "))
term=int(input("Enter the Number of Terms: "))
sum1=0
s=0
for i in range(term):
    s=s+(10**i)*5
    sum1+=s
print(f"Sum of series of {term} terms is {sum1}")