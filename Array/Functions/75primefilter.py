## Use filter() to extract all prime numbers from a list.
num=[2,4,5,7,8]
is_prime=list(filter(lambda n:n>1 and all( n%i!=0 for i in range(2,int(n**0.5)+1)),num))
print("Original number:",num)
print("Prime numbers in a list:",is_prime)