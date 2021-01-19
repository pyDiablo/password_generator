"""

    Password Generator
    Written by: @pyDiablo

    Generates a password of a given length
    and copies it to the clipboard.

"""

import random
import pyperclip
import sys


# Constants
CHARACTER_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890,.<>?;:"=+-_*&^%$#@!`~'  # Length of the string is 84


def generate_password(length):
    """ Generates a password of a given length and copies it to the clipboard """

    password = ''
    for i in range(length):
        num = random.randint(0, len(CHARACTER_SET) - 1)  # Creates a random integer between 0 and 83 (both inclusive)
        password += CHARACTER_SET[num]  # Appends a random character from character set to the end of the password
    return password


def copy_to_clipboard(some_string):
    """ Copies the given string to clipboard """

    pyperclip.copy(some_string)  # Copy password to clipboard using pyperclip
    print('Password copied to clipboard!')


def main(length=None):
    # When no argument is provided
    if length is None:
        try:
            password_length = int(input('\nPassword length: '))  # Length of password to be generated
        except ValueError:
            print("Error: password's length should be an integer!")  # Print this if user enters any value other than integer
        else:
            # If user enters a negative integer
            if password_length < 0:
                password_length *= -1
            print('Generating...')
            password = generate_password(password_length)
            print(password)
            copy_to_clipboard(password)
    # When argument is provided
    else:
        try:
            password_length = int(length)
        except ValueError:
            print("Error: password's length should be an integer!")  # Print this if user enters any value other than integer
        else:
            # If user enters a negative integer
            if password_length < 0:
                password_length *= -1
            print('Generating...')
            password = generate_password(password_length)
            print(password)
            copy_to_clipboard(password)


if __name__ == '__main__':
    try:
        main(sys.argv[1])  # When user provides a command line argument
    except IndexError:
        main()  # When no argument is provided
