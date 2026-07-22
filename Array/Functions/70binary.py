## Implement Binary Search using recursion.
def binary(low,high,arr,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]>key:
        return binary(low,mid-1,arr,key)
    elif arr[mid]<key:
        return binary(mid+1,high,arr,key)
    else:
        return mid
arr=[]
n=int(input("Enter the size of an array:"))
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the number to search:"))
res=binary(0,n-1,arr,key)
if res!=-1:
    print("Element is found at index:",res)
else:
    print("Element  not found in the array")            
    

