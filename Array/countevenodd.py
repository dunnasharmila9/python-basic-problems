arr=[]
n=int(input("Enter the size of an array:"))
for i in range(n):
    k=int(input())
    arr.append(k)
even=0
odd=0    
for i in range(n):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print("No of even elements:",even)
print("no.of odd elements",odd)                