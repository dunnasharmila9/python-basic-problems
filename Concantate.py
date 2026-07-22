##11.Convert an integer into a string and concatenate it with another string
user_integer = int(input("Enter an integer: "))
user_string = input("Enter a string: ")

converted_string = str(user_integer)
result = converted_string + user_string

print("Concatenated result:", result)