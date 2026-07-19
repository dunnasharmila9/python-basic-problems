x = float(input("Enter initial value: "))
y = float(input("Enter second number: "))

x += y
print(f"After += : {x}")

x -= y
print(f"After -= : {x}")

x *= y
print(f"After *= : {x}")

x /= y
print(f"After /= : {x}")

x //= y
print(f"After //= : {x}")

x %= y
print(f"After %= : {x}")

x **= y
print(f"After **= : {x}")