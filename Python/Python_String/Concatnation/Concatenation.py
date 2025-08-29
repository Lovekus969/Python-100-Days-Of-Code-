
# Example of String Concatenation in Python

#  Correct concatenation with strings
first_name = "Kush"
last_name = "Singh"
full_name = first_name + " " + last_name
print(full_name)  # Output: Kush Singh


# ❌ Error example: trying to concatenate string with integer directly
age = 25
# print("I am " + age + " years old")  # TypeError: can only concatenate str (not "int") to str


#  Fix 1: Convert integer to string using str()
print("I am " + str(age) + " years old")


#  Fix 2: Use f-strings (recommended)
print(f"I am {age} years old")


# Fix 3: Using format() method
print("I am {} years old".format(age))
