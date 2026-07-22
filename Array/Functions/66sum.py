## Find the sum of digits of a number using recursion.
def sum(num):
    if num<10:
        return num
    else:
        return (num%10)+sum(num//10)
num=int(input("Enter the number:"))
result=sum(num)
print(f"sum of a digits of a number {num}:",result)    