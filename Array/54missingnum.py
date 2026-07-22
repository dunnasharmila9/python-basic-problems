##Find the missing number from an array containing numbers from 1 to N.
arr=[]
n=int(input("Enter the size of an array:"))
for i in range(n):
    arr.append(int(input()))  
for i in range(1,n+1):
    if i not in arr:
        print("Missing number:",i)
        break
