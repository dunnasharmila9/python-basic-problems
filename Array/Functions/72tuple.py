##Sort a list of tuples based on the second value using a lambda function.
students = [("Sharmila", 85), ("Rahul", 92), ("Amit", 78), ("Priya", 95)]
print("Original list:")
print(students)
sorted_students = sorted(students, key=lambda item: item[1])

print("\nSorted list (based on second value):")
print(sorted_students)