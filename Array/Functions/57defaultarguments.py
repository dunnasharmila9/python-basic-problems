##Create a function to calculate student percentage using default arguments.
def calculate( m1,m2,m3,m4=34,m5=52):
    total=(m1+m2+m3+m4+m5)
    percentage=int((total/500)*100)
    return percentage
result=calculate(50,100,30)
print("Percentage of a Student:",result)
