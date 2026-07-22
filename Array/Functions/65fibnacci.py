## Generate Fibonacci series using recursion.
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
terms=int(input("Enter the no.of terms: "))
if terms<=0:
    print("Enter the positive term")
else:
    print("fibnacci series:")
    for i in range(terms):
        print(fibonacci(i),end=" ")        
