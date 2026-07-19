arr1=[]
n=int(input("Enter the size of an array 1:"))
for i in range(n):
    arr1.append(int(input()))
arr2=[]
n1=int(input("Enter the size of the array 2:"))
for i in range(n1):
    arr2.append(int(input()))
merge=[0]*(n+n1)
i=0
for k in range(n):
    merge[i]=arr1[k]
    i+=1
for k in range(n1):
    merge[i]=arr2[k]
    i+=1
print(merge)        
    

