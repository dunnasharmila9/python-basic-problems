## 10.Convert a string containing a number into an integer and perform addition.
user_string = input("Enter a number as a string: ")
number_to_add = int(input("Enter another integer to add to it: "))

converted_integer = int(user_string)
total_sum = converted_integer + number_to_add

print("Result after addition:", total_sum)