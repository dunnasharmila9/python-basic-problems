##47.Reverse an array without using built-in reverse functions.
arr=[]
n=int(input("Enter the size of an array:"))
for i in range(n):
    val=int(input())
    arr.append(val)
print("Reverse of the element:")    
for j in range(n-1,-1,-1):
    print(arr[j])    