##44.Calculate the sum of all elements in an array without using the sum() function.
from array import*
arr=array("i",[])
n=int(input("Enter the size of array:"))
for i in range(n):
    value=int(input(f"Enter the value {i+1}:"))
    arr.append(value)
sum=0    
for j in range(n):
    sum+=arr[j]
print("Total sum of the elements:",sum)    