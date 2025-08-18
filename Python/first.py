# first.py
# Day 1: Python Basics

print("Hello",end=" ")
print("Python World!")

# Variables
x = 10
name = "Kush"
pi = 3.1415
print(f"My name is {name}, x={x}, pi={pi}")

# Loops
print("Numbers from 1 to 5:", end=" ")
for i in range(1, 6):
    print(i, end=" ")
print()  # new line

#  Function example
def square(n):
    return n * n

print("Square of 7 is:", square(7))

