## 53.Implement Linear Search to find an element in an array.
arr=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
    arr.append(int(input()))
k=int(input("Enter the element to be find:"))
i=0
found=False
for e in arr:
    i+=1
    if e==k:
        print(f"Element is found at index {i}")
        found=True
if found==False:
    print("Element not found")              