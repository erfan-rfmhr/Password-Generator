import string
import random
import os
os.system('cls')

length = 6
upper = True
lower = True
symbol = True
number = True
space = False

def generate_password(password_length, have_uppercase, have_lowercase, have_symbol, have_number, have_space):
    """Generates a password"""
    print()
    print(10*'*', "Generate Password", 10*'*')

    print(f"""Active settings:

Password length: {password_length}
Uppercase: {have_uppercase}
Lowercase: {have_lowercase}
Symbols: {have_symbol}
Number: {have_number}
Space: {have_space}
""")

    counter = 0
    password = ''

    while counter != password_length:
        random_item = random.choice(list(range(5)))

        match random_item:
            case 0:
                if have_uppercase == True:
                    password += random.choice(string.ascii_uppercase)
                    counter += 1
                    continue
            case 1:
                if have_lowercase == True:
                    password += random.choice(string.ascii_lowercase)
                    counter += 1
                    continue
            case 2:
                if have_symbol == True:
                    password += random.choice(string.punctuation)
                    counter += 1
                    continue
            case 3:
                if have_number == True:
                    password += random.choice(string.digits)
                    counter += 1
                    continue
            case 4:
                if have_space == True:
                    password += ' '
                    counter += 1
                    continue

    print(f"""
*There is no space before the first character of password. If there is, password includes spaces.
*The /S*P*A*C*E/ helps you to know if there is a space at the end of the password.
Generated password:
{password}/S*P*A*C*E/
""")


def setting():
    """setting() function gets settings from user"""
    password_length = 6
    have_uppercase = True
    have_lowercase = True
    have_symbol = True
    have_number = True
    have_space = False

    print()
    print(10*'*', "Setting", 10*'*')
    password_length = int(input("Password length: "))
    print('\nPress "Enter" key for "Yes" or type anything then enter for "No".')
    print("\nDoes the password have...")
    if not input("uppercase letters? "):
        have_uppercase = True
    else:
        have_uppercase = False

    if not input("lowercase letters? "):
        have_lowercase = True
    else:
        have_lowercase = False

    if not input("symbols? "):
        have_symbol = True
    else:
        have_symbol = False

    if not input("numbers? "):
       have_number = True
    else:
       have_number = False

    if not input("spaces? "):
        have_space = True
    else:
        have_space = False

    generate_password(password_length, have_uppercase, have_lowercase, have_symbol, have_number, have_space)

    return password_length, have_uppercase, have_lowercase, have_symbol, have_number, have_space


def display_menu():
    """display_menu() function displays the main menu"""
    print()
    print(10*'*', "Menu", 10*'*')
    print("1. Setting\n2. Generate")
display_menu()


def main_menu():
    """this function calls setting and generate password function"""
    global length, upper, lower, symbol, number, space
    choice = input("Enter the desired option (* to exit): ")
    while choice != '*':
        match choice:
            case '1':
                length, upper, lower, symbol, number, space = setting()
            case '2':
                generate_password(length, upper, lower, symbol, number, space)
        display_menu()
        choice = input("Enter the desired option (* to exit): ")
main_menu()