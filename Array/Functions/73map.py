## Use map() to convert a list of Celsius temperatures into Fahrenheit.
num=[56,47,80,23]
cf=list(map(lambda c:(c*9/5)+32,num))
print(cf)
