
M=int(input("Enter the time in minute:"))
S=int(input("Enter the time in Second:"))
h=(M//60)
rm=M%60
print("No.of hours:",h)
print("Remaining minute:",rm)
SH=S//3600
SM=(S%3600)//60
SS=(S%3600)%60
print("Seconds to hour:",SH)
print("NO of hours:",SH)
print("remaining minute left after conversion from  seconds to hour:",SM)
print("remaining second left after conversion from seconds to hour:",SS)