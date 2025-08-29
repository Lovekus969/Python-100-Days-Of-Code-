s = "Hello World"
encoded_s = s.encode()  # default utf-8
print(encoded_s)         # b'Hello World'

# Using different encoding
print(s.encode('ascii'))  # b'Hello World'
