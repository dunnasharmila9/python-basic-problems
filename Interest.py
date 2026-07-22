##22.Calculate the simple interest for given principal, rate, and time.
##23.Calculate the compound interest for given principal, rate, and time

a=float(input("Enter the Principle:"))
b=float(input("Enter the rate:"))
c=float(input("Enter the time:"))
n=1
d=(a*b*c)/100
compoundinterest=a*pow((1+(b/100)/n),c*n)-a
print("Compound Interest=",compoundinterest)
print("Simple Interest:",d)