##Count the number of occurrences of a given element in an array
arr=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
    arr.append(int(input()))
dict={}
for e in arr:
    if e in dict:
        dict[e]+=1
    else:
        dict[e]=1
k=int(input("Entert the Element to find occurance: "))
print(f"Occurance of an Element {k}:",dict[k])                
    