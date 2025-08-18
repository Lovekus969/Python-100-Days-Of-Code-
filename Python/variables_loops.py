
# Day 2: Variables and Loops in Python

# Variables
age = 22
name = "Kush"
height = 5.9
is_student = True

print(f"My name is {name}, age = {age}, height = {height}, student = {is_student}")

# Lists and Loops
numbers = [1, 2, 3, 4, 5]

# For loop
print("Numbers in the list:", end=" ")
for num in numbers:
    print(num, end=" ")
print()  # newline

# While loop
print("Numbers using while loop:", end=" ")
i = 0
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1
print()

#  Simple operations inside loop
print("Squares of numbers:", end=" ")
for num in numbers:
    print(num**2, end=" ")
print()
