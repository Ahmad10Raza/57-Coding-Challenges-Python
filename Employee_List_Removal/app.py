# Sometimes you have to locate and remove an entry from a
# list based on some criteria. You may have a deck of cards
# and need to discard one so it’s no longer in play, or you may
# need to remove values from a list of valid inputs once they’ve
# been used. Storing the values in an array makes this process
# easier. Depending on your language, you may find it safer
# and more efficient to create a new array instead of modifying
# the existing one.
# Create a small program that contains a list of employee
# names. Print out the list of names when the program runs
# the first time. Prompt for an employee name and remove
# that specific name from the list of names. Display the
# remaining employees, each on its own line.
# Example Output
# There are 5 employees:
# John Smith
# Jackie Jackson
# Chris Jones
# Amanda Cullen
# Jeremy Goodwin
# Enter an employee name to remove: Chris Jones
# There are 4 employees:
# John Smith
# Jackie Jackson
# Amanda Cullen
# Jeremy Goodwin
# Constraint
# • Use an array or list to store the names.


import random

employees = [
    'John Smith',
    'Jakie Jackson',
    'Chris Jones',
    'Amanda Cullen',
    'Jeremy Goodwin',
]

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Employee list removal \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def print_employees():
    number_of_employees = len(employees)
    print(f'There are {number_of_employees} employees:')
    for employee in employees:
        print(employee) 


def get_employee_name():
    while True:
        employee_name = input('Enter an employee name to remove: ')
        if len(employee_name) > 0:
            return employee_name
        else:
            print('A valid input is required')


def remove_employee(employee_name):
    if employee_name in employees:
        employees.remove(employee_name)



if __name__ == "__main__":
    print_header()
    print_employees()
    employee_name = get_employee_name()
    remove_employee(employee_name)
    print_employees()