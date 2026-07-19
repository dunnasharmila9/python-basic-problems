arr=[]
n=int(input("Enter the no of elements:"))
for i in range(n):
    v=int(input())
    arr.append(v)
k=int(input("Enter the no of postions to rotate:"))
k=k%n    
for j in range(k):
        temp=arr[n-1]
        for p in range(n-1,0,-1):
            arr[p]=arr[p-1]
        arr[0]=temp
print(arr)            