##44.Find the largest element in an array without using the max() function.
##45.Find the smallest element in an array without using the min() function

arr=[]
n=int(input("Enter the array size:"))
for j in range(n):
    k=int(input())
    arr.append(k)
max=arr[0]
min=arr[0]
for i in range(n):
    if max<arr[i]:
        max=arr[i]
    if min>arr[i]:
        min=arr[i]
print("Maximum Element in given array:",max)
print("Minimum Element in the given  array:",min)                