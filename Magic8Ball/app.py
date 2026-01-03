# Arrays are great for storing possible responses from a pro-
# gram. If you combine that with a random number generator,
# you can pick a random entry from this list, which works
# great for games.
# Create a Magic 8 Ball game that prompts for a question and
# then displays either “Yes,” “No,” “Maybe,” or “Ask again
# later.”
# Example Output
# What's your question?
#  Will I be rich and famous?
# Ask again later.
# Constraint
# • The value should be chosen randomly using a pseudo
# random number generator. Store the possible choices
# in a list and select one at random.



import random

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Magic 8 Ball \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_question():
    while True:
        question = input('What\'s your question? ')
        if len(question) > 0:
            return question
        else:
            print('A valid input is required')

def print_response():
    responses = ['Yes', 'No', 'Maybe', 'Ask again later.']
    response = random.choice(responses)
    print(response)

if __name__ == "__main__":
    print_header()
    get_question()
    print_response()