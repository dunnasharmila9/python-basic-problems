## Use filter() to extract all even numbers from a list.
num=[]
n=int(input("Enter the size of a list:"))
for i in range(n):
    num.append(int(input()))
even_num=list(filter(lambda e:e%2==0,num))
print(even_num)    
## Use filter() to extract all prime numbers from a list.

