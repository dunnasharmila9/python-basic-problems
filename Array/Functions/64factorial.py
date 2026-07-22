def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("Enter the Number to find the factorial:"))
result=factorial(num)
print(f"Fctorial of a number {num} is:",result)
    

