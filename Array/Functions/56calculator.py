##Create a calculator program using separate functions for addition, subtraction, multiplication, and division.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
p=int(input("Enter the first number:"))
q=int(input("Enter the second number:"))
r1=add(p,q)
r2=sub(p,q)
r3=mul(p,q)
r4=div(p,q)
print("Multiplication of two number:",r3)
print("addition of two numbers:",r1)
print("subtraction of two numbers:",r2)
print("division of two numbers:",r4)