min_length = 8

while True:
    password = input("Enter a password: ")

    if len(password) >= min_length:
        break
    else:
        print(f"Password must be at least {min_length} characters long.")

print('*' * len(password))
