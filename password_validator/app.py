
import getpass

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Password Complexity Checker \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_password():
    """Gets password from user input."""
    password = getpass.getpass('Enter a password to check its complexity: ')
    return password


def check_password_complexity(password):
    """
    Determines the complexity of a given password based on a set of rules.
    """
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    # A character is special if it's not a letter and not a digit.
    has_special = not all(c.isalnum() for c in password)

    if has_numbers and not has_letters and not has_special and length < 8:
        return "very weak"
    elif has_letters and not has_numbers and not has_special and length < 8:
        return "weak"
    elif has_letters and has_numbers and not has_special and length >= 8:
        return "strong"
    elif has_letters and has_numbers and has_special and length >= 8:
        return "very strong"
    else:
        return "of unknown strength"


def print_result(password, strength):
    """Prints the result of the password complexity check."""
    if strength != "of unknown strength":
        print(f"The password '{password}' is a {strength} password.")
    else:
        print(f"The password '{password}' does not fit the defined complexity rules.")

    
if __name__ == "__main__":
    print_header()
    password = get_password()
    if password:
        strength = check_password_complexity(password)
        print_result(password, strength)