def find_max(array):
    if len(array)==1:
        return array[0]
    else:
        sub_max=find_max(array[1:])
        if array[0]>sub_max:
            return array[0]
        else:
            return sub_max
arr=[]
n=int(input("Enter the size of an array:"))
for i in range(n):
    arr.append(int(input()))
res=find_max(arr)
print("maximum emlement of an array:",res)     