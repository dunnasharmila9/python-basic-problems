## Create a function that returns multiple values such as sum, difference, and multiplication.
def calculate_all(num1,num2):
    total_sum=num1+num2
    total_difference=num1-num2
    multiplication=num1*num2
    return total_sum,total_difference,multiplication
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
s,d,m=calculate_all(num1,num2)
print("Sum of two numbers:",s)
print("difference of two numbers:",d)
print("multiplication of two numbers:",m)
