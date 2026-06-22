import random

def generate_password():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    length = int(input("Enter password length: "))

    if length < 6:
        print("Password length should be at least 6")
        return

    password = random.choice(upper)
    password += random.choice(lower)
    password += random.choice(numbers)

    all_characters = upper + lower + numbers

    for i in range(length - 3):
        password += random.choice(all_characters)

    password_list = list(password)
    random.shuffle(password_list)

    final_password = "".join(password_list)

    print("Generated Password:", final_password)

generate_password()