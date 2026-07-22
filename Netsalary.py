##32.Calculate the salary after adding HRA and DA and deducting tax.
HRA=float(input("Enter the Home rent Allowance(HRA):"))
DA=float(input("Enter the Dearness Allowance(DA):"))
S=float(input("Enter the Base Salary:"))
tax=float(input("Enter the dedection tax:"))
GrossSalary=S+HRA+DA
netsalary=GrossSalary-tax
print("Monthly salary earned=",netsalary)
          
