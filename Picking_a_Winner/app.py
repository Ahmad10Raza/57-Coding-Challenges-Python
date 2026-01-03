# Arrays don’t have to be hard-coded. You can take user input
# and store it in an array and then work with it.
# Create a program that picks a winner for a contest or prize
# drawing. Prompt for names of contestants until the user
# leaves the entry blank. Then randomly select a winner.
# Example Output
# Enter a name: Homer
# Enter a name: Bart
# Enter a name: Maggie
# Enter a name: Lisa
# Enter a name: Moe
# Enter a name:
# The winner is... Maggie.
# Constraints
# • Use a loop to capture user input into an array.
# • Use a random number generator to pluck a value from
# the array.
# • Don’t include a blank entry in the array.
# • Some languages require that you define the length of
# the array ahead of time. You may need to find another
# data structure, like an ArrayList.


import random

names = list()

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Picking a Winner \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_name():
    while True:
        employee_name = input('Enter a name: ')
        if len(employee_name) > 0:
            return employee_name
        else:
            print('A valid input is required')

def get_names():
    for i in range(6):
        name = get_name()
        names.append(name)

def pick_name():
    name = random.choice(names)
    return name


def print_winner(winner_name):
    print(f'The winner is... {winner_name}')


if __name__ == "__main__":
    print_header()
    get_names()
    winner_name = pick_name()
    print_winner(winner_name)