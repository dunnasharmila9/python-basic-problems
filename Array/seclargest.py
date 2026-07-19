arr=[]
n=int(input("Enter the size of an array:"))
for i in range(n):
    v=int(input())
    arr.append(v)
largest=arr[0]
secondlargest=arr[0]    
for a in arr:
    if a>largest:
        largest=a
        secondlargest=largest
    elif secondlargest>a<largest:
        secondlargest=a
print("Second largest element:",a)



