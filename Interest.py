a=float(input("Enter the Principle:"))
b=float(input("Enter the rate:"))
c=float(input("Enter the time:"))
n=1
d=(a*b*c)/100
compoundinterest=a*pow((1+(b/100)/n),c*n)-a
print("Compound Interest=",compoundinterest)
print("Simple Interest:",d)