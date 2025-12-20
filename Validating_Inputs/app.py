# Large functions aren’t very usable or maintainable. It makes
# a lot of sense to break down the logic of a program into
# smaller functions that do one thing each. The program can
# then call these functions in sequence to perform the work.
# Write a program that prompts for a first name, last name,
# employee ID, and ZIP code. Ensure that the input is valid
# according to these rules:
# • The first name must be filled in.
# • The last name must be filled in.
# • The first and last names must be at least two characters
# long.
# • An employee ID is in the format AA-1234. So, two let-
# ters, a hyphen, and four numbers.
# • The ZIP code must be a number.
# Display appropriate error messages on incorrect data.
# Example Output
# Enter the first name: J
# Enter the last name:
# Enter the ZIP code: ABCDE
# Enter an employee ID: A12-1234
# "J" is not a valid first name. It is too short.
# The last name must be filled in.
# The ZIP code must be numeric.
# A12-1234 is not a valid ID.
# Or
# Enter the first name: Jimmy
# Enter the last name: James
# Enter the ZIP code: 55555
# Enter an employee ID: TK-421
# There were no errors found.

import re

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Validating Input\n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_first_name():
    while True:
        first_name = input('Enter the first name: ')
        if first_name.isalpha() and len(first_name) >= 2:
            return first_name
        else:
            print('The first name must be filled in and at least two characters long.')


def get_last_name():
    while True:
        last_name = input('Enter the last name: ')
        if last_name.isalpha() and len(last_name) >= 2:
            return last_name
        else:
            print('The last name must be filled in and at least two characters long.')


def get_employee_id():
    while True:
        regex = '^[A-Z]{2}-[0-9]{4}$' # two letters, a hyphen, and four numbers
        employee_id = input("Enter an employee ID: ")
        if re.match(regex, employee_id):
            return employee_id
        else:
            print('A valid input is required')

if __name__ == "__main__":
    print_header()
    first_name = get_first_name()
    last_name = get_last_name()
    employee_id = get_employee_id()
    if all([first_name, last_name, employee_id]):
        print('There were no errors found.')