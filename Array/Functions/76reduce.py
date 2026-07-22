## Use reduce() to find the product of all elements in a list.
from functools import reduce
list=[3,1,2,5]
product=reduce(lambda x,y:x*y,list)
print("product of the numbers in a list=",product)