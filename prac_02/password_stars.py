def main():
    min_length = 8

    password = get_password(min_length)

    print_password(password)


def print_password(password):
    print('*' * len(password))


def get_password(min_length):
    while True:
        password = input("Enter a password: ")

        if len(password) >= min_length:
            break
        else:
            print(f"Password must be at least {min_length} characters long.")
    return password


main()
