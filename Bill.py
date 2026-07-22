##36.Calculate the total bill including GST.
U=int(input("Enter the no of units consumed:"))
R=float(input("Enter the cost per one unit:"))
GST=float(input("Enter the GST:"))
TC=U*R+GST
print("Total amount to be paid=",TC)
