## Find the duplicate element present in an array.
arr=[]
n=int(input("Enter the size of an array:"))
for i in range(n):
    arr.append(int(input()))
dict={}
for e in arr:
    if e in dict:
        dict[e]+=1
    else:
        dict[e]=1
for key,value in dict.items():
    if value==2:
        print("The duplicate element:",key)
