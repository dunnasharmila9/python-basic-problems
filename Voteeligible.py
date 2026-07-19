age = int(input("Enter student age: "))
is_citizen = input("Is the student a citizen? (yes/no): ").strip().lower() == "yes"
is_eligible = (age >= 18) and is_citizen
print("Voting eligibility status:", is_eligible)