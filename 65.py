import random
import string

def generate_password():
    upper_case = random.choice(string.ascii_uppercase)
    lower_case = random.choice(string.ascii_lowercase)
    number = random.choice(string.digits)
    remaining_length = 5  
    partial_password = upper_case + lower_case + number

    for _ in range(remaining_length):
        char_type = random.choice([string.ascii_uppercase, string.ascii_lowercase, string.digits])
        partial_password += random.choice(char_type)

    password_list = list(partial_password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

if __name__ == "__main__":
    num_passwords = 100
    password_width = 8

    passwords = []
    for _ in range(num_passwords):
        password = generate_password()
        passwords.append(password)

    for x, password in enumerate(passwords, 1):
        print(f"Password {x:3}: {password}")
