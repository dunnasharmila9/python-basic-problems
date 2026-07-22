##Implement Binary Search on a sorted array
arr=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
    arr.append(int(input()))
low=0
high=n-1
E=int(input("Enter the element to found:"))
found=False
while(low<=high):
    mid=((low+high)//2)
    if E<arr[mid]:
        high=mid-1
    elif E>arr[mid]:
        low=mid+1
    elif E==arr[mid]:
        print(f"Element is found at index {mid}:")
        found=True
        break
if found==False:
    print("The element is not found")                     
