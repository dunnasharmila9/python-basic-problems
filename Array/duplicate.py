arr=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
    v=int(input())
    arr.append(v)
uni=[]
print("After removing Array elements are:")
for e in arr:
    if e not in uni:
        uni.append(e)
print(uni)        
