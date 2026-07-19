CP=float(input("Enter the cost price of an item:"))
SP=float(input("Enter the selling price of an item:"))
if SP>CP:
    profit=SP-CP
    print("Profit=",profit)
else:
    loss=CP-SP
    print("loss =",loss)    
