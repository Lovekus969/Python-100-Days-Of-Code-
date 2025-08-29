
# Python String Examples - All in One

# =======================
# 1. String Concatenation
# =======================
first_name = "Kush"
last_name = "Singh"
full_name = first_name + " " + last_name
print(full_name)  # Kush Singh

age = 25
# ❌ Error: concatenating string with int directly
# print("I am " + age + " years old")  # TypeError

# ✅ Fix 1: Convert int to string
print("I am " + str(age) + " years old")

# ✅ Fix 2: Using f-string (preferred)
print(f"I am {age} years old")

# ✅ Fix 3: Using format()
print("I am {} years old".format(age))

# =======================
# 2. F-Strings with Placeholders and Modifiers
# =======================
price = 49.9876
quantity = 3
name = "kush"

# Simple f-string
print(f"My name is {name} and I am {age} years old")

# Expression inside placeholder
print(f"Total cost: ${price * quantity:.2f}")  # 2 decimal places

# Function call inside placeholder
print(f"Name in uppercase: {name.upper()}")

# Alignment and padding
print(f"|{'Left':<10}|{'Center':^10}|{'Right':>10}|")

# =======================
# 3. Escape Characters
# =======================
# Quotes inside strings
text = "He said, "Hello World""
print(text)

# Newline
print("Hello\nWorld")  # literal 

print("Hello
World")   # actual newline

# Tab
print("Name	Age")

# Backslash
print("This is a backslash: \\")  # prints a single backslash

# Unicode
print("❤")  # ❤

# =======================
# 4. String Slicing & Step/Reverse
# =======================
s = "FAANG"
print(s[1:4])     # 'AAN'
print(s[:4])      # 'FAAN'
print(s[2:])      # 'ANG'
print(s[::-1])    # 'GNAAF' (reverse)
print(s[::-2])    # 'GA' (reverse every other character)

# =======================
# 5. Palindrome Check
# =======================
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("racecar")) # True
print(is_palindrome("hello"))   # False
