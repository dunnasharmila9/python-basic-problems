## Create a function to check whether a given number is prime or not.
def isprime(num):
    if num<=1:
        print("It is not a prime number:")
    for i in range(2,num):
        if(num%i==0):
            print("It is a  not prime number")
            break
    else:
        print("It is a prime number:")    
num=int(input("Enter the number to find:"))
isprime(num)        