# Example with dictionary (checks only keys, not values)
student = {"id": 101, "name": "Kush"}

print("id" in student)         #  True
print("Kush" in student)       #  False (because "Kush" is a value)
print("name" not in student)   #  False
