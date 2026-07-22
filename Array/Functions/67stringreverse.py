## Reverse a string using recursion.
def reverse(string):
    if len(string)<=1:
        return string
    else:
        return reverse(string[1:])+string[0]
s=input("Enter the string:")
result=reverse(s)
print("Reverse of  a string is:",result)        