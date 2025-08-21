# day2.py
# Python Day 2: Variables, Syntax, For Loop, and Dynamic Typing

def main():
    # --- Variables ---
    name = "Kush"      # string
    age = 21           # integer
    height = 5.9       # float
    is_student = True  # boolean

    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Student:", is_student)

    print("\n--- Dynamic Typing ---")
    x = 10
    print("x =", x, "| type:", type(x))  # int

    x = "Hello Python"
    print("x =", x, "| type:", type(x))  # str

    x = 3.14
    print("x =", x, "| type:", type(x))  # float

    # --- For Loop Examples ---
    print("\n--- For Loop with range ---")
    for i in range(5):
        print("Number:", i)

    print("\n--- For Loop through list ---")
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print("I like", fruit)

    print("\n--- For Loop through string ---")
    for letter in "Python":
        print(letter)

    # --- Small Task ---
    print("\n--- Squares from 1 to n ---")
    n = 7
    for i in range(1, n + 1):
        print(f"Square of {i} is {i * i}")

if __name__ == "__main__":
    main()
