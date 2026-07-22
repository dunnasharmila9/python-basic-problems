## Calculate the power of a number using recursion.
def power(Base,Exponent):
    if Exponent==0:
        return 1
    else:
        return Base*power(Base,Exponent-1)
b=int(input("Enter the base: "))
e=int(input("Enter the exponenet:"))
res=power(b,e)
print("Power of the value=",res)    

  