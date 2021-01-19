"""

    Password Generator
    Written by: @pyDiablo

    Generates a password of a given length
    and copies it to the clipboard.

"""

import random
import pyperclip


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


def main():
    password_length = int(input('\nPassword length: '))  # Length of password to be generated
    print('Generating...')
    password = generate_password(length=password_length)
    print(password)
    copy_to_clipboard(password)


if __name__ == '__main__':
    main()
