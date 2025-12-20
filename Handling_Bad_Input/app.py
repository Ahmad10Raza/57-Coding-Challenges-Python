# The rule of 72 is a quick method for estimating how long it
# will take to double your investment, by taking the number
# 72 and dividing it by the expected rate of return. It’s a good
# tool that helps you figure out if the stock, bond, or savings
# account is right for you. It’s also a good program to write to
# test for and prevent bad input because computers can’t
# divide by zero. And instead of exiting the program when
# the user enters invalid input, you can just keep prompting
# for inputs until you get one that’s valid.
# Write a quick calculator that prompts for the rate of return
# on an investment and calculates how many years it will take
# to double your investment.
# The formula is
# years = 72 / r
# where r is the stated rate of return.
# Example Output
# What is the rate of return? 0
# Sorry. That's not a valid input.
# What is the rate of return? ABC
# Sorry. That's not a valid input.
# What is the rate of return? 4
# It will take 18 years to double your initial investment.


def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Handling Bad Input \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)
    

def get_rate():
    while True:
        try:
            rate = int(input("Enter the rate of return? "))
            return rate
        except ValueError:
            print("Sorry! That's not valid input.")
            
def get_investment(rate):
    return 72/rate

def print_investment(rate):
    print(f"It will talke {get_investment(rate)} years to double your initial investment.")
    
if __name__ == '__main__':
    print_header()
    rate = get_rate()
    print_investment(rate)
