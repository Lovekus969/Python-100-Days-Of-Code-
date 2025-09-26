# Key = Product ID, Value = Product Name
products = {
    101: "Milk",
    102: "Rice",
    103: "Shampoo"
}

# Access product by ID
print(products[101])   # Milk

# Insert new product
products[104] = "Soap"

# Search product
if 102 in products:
    print(products[102])  # Rice
