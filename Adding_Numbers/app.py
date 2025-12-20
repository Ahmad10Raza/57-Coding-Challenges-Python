from ast import While
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


def get_numbers():
    numbers = list()
    while len(numbers) != 5:
        try:
            number = int(input("Enter Number:"))
            numbers.append(number)
        except ValueError:
            print("Enter Value Number!")
    return numbers


def get_sum():
    return sum(get_numbers())

def print_sum():
    print(f"The sum of the numbers is: {get_sum()}")

if __name__ == "__main__":
    print_header()
    print_sum()