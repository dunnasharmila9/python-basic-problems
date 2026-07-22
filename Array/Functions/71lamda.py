## Use a lambda function to find the square of each element in a list.
num=[]
n=int(input("Enter the size of the list:"))
for i in range(n):
    num.append(int(input()))
sq_list=list(map(lambda x:x*x,num))
print("Squares of a number in a list:")
print(sq_list)    
