'''
emails task
Estimated time: 25 minutes
Actual time: 35 minutes
'''

def extract_name(email):
    username = email.split('@')[0]
    name_parts = username.split('.')
    name = ' '.join(name_parts).title()
    return name


user_data = {}

email = input("Email: ")
while email != "":
    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").lower()

    if confirmation != "y" and confirmation != "":
        name = input("Name: ")

    user_data[email] = name
    email = input("Email: ")

for email, name in user_data.items():
    print(f"{name} ({email})")
