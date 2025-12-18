# Problem Statement: Months to Pay Off Credit Card Balance
#
# Write a program that determines how many months it will take to pay off a credit
# card balance. The program should:
# 1. Prompt the user to enter the credit card balance (in dollars).
# 2. Prompt for the APR (annual percentage rate) as a percent.
# 3. Prompt for the monthly payment amount (in dollars).
# 4. Calculate the number of months required to pay off the balance using the
#    standard financial formula:
#        n = -log(1 - (B * i_monthly) / P) / log(1 + i_monthly)
#    where:
#        B = balance,
#        P = monthly payment,
#        i_monthly = APR / 1200  (monthly interest rate as a decimal).
# 5. Output the result, e.g., "It will take you X months to pay off this card."
#
# Example interaction:
#   What is your balance? 5000
#   What is the APR on the card (as a percent)? 12
#   What is the monthly payment you can make? 100
#   It will take you 70 months to pay off this card.
#
# Note: If the monthly payment is too low to ever reduce the balance, the program
# should indicate that the payment is insufficient


import math

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Months to Pay Off a Credit Card \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_balance():

    while True:
        try:
            balance = input('What is your balance? ')
            return int(balance)
        except ValueError:
            print('A valid input is required')


def get_apr():

    while True:
        try:
            apr = input('What is the APR on the card (as a percent)? ')
            return int(apr)
        except ValueError:
            print('A valid input is required')


def get_monthly_payments():

    while True:
        try:
            monthly_payment = input('What are the monthly payment you can make? ')
            return int(monthly_payment)
        except ValueError:
            print('A valid input is required')


def calculate_months_until_paid_off(balance: int, apr: int, monthly_payment: int) -> int:
    """ Calculate the number of months required to pay off a credit card balance. """
    apr = apr / 100
    apr = apr / 365
    month_until_paid_off = (-1/30) * math.log(1 + (balance / monthly_payment) * (1 - (1 + apr) ** 30),10) / math.log(1 + apr,10)
    return math.ceil(month_until_paid_off)
    
def print_months_take_to_pay(months):
    print(f'It will take you {months} months to pay off this card')

if __name__ == "__main__":
    print_header()
    balance = get_balance()
    apr = get_apr()
    monthly_payments = get_monthly_payments()
    months_until_paid_off = calculate_months_until_paid_off(balance, apr, monthly_payments)
    print_months_take_to_pay(months_until_paid_off)
