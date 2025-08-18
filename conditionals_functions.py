
# Day 3: Conditionals and Functions in Python

#Conditional statements
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Nested conditionals
score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Your score is {score}, grade = {grade}")

# Functions
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

print(greet("Kush"))
print("Sum of 5 and 7 is:", add(5, 7))

# Function with condition
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number 10 is", check_even_odd(10))
print("Number 7 is", check_even_odd(7))
