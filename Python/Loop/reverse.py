num = 12345
rev = 0

while num > 0:
    digit = num % 10       # get last digit
    rev = rev * 10 + digit # add it to reversed number
    num = num // 10        # remove last digit

print(rev)  # 54321
