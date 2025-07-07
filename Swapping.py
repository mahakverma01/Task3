# Swap Two Numbers (No third variable)

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping without a third variable
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")