import random
import string

def print_header():
    """ Print header 
    """
    # Initialize an empty string to build the header
    header_text = ''
    
    # Define the main title text with newline
    TEXT = f' Sorting records \n'
    
    # Create a line of dashes matching the length of TEXT
    line = '-' * len(TEXT)
    line += '\n'

    # Build the header: top line, title, bottom line
    header_text += line
    header_text += TEXT
    header_text += line
    
    # Display the complete header
    print(header_text)


# List of user dictionaries containing employee information
users = [
    {'first_name':'John', 'last_name':'Johnson', 'position':'Manager', 'separation_date':'2016-12-31'},
    {'first_name':'Tou', 'last_name':'Xiong', 'position':'Software Engineer', 'separation_date':'2016-10-05'},
    {'first_name':'Michaela', 'last_name':'Michaelson', 'position':'District Manage', 'separation_date':'2015-12-19'},
    {'first_name':'Jake', 'last_name':'Jacobson', 'position':'Programmer', 'separation_date':''},
    {'first_name':'Jacquelyn', 'last_name':'Jackson', 'position':'DBA', 'separation_date':''},
    {'first_name':'Sally', 'last_name':'Weber', 'position':'Web Developer', 'separation_date':'2015-12-18'}
]


def print_headings():
    """ Print column headings for the user table
    """
    # Define the column headers
    headings = ['First Name', 'Last Name', 'Position', 'Separation date']
    
    # Loop through each heading with its index
    for index, heading in enumerate(headings):
        # Check if this is the last heading
        if index == len(headings)-1:
            # Print the last heading with a newline (default behavior)
            print(heading)
        else:    
            # Print heading followed by pipe separator (no newline)
            print(heading, end='|')
    
    # Print an empty line after headings
    print()


def print_users():
    """ Print all user records in a formatted table
    """
    # Iterate through each user dictionary
    for user in users:
        # Iterate through each key-value pair in the user dictionary
        for key, value in user.items():
            # ALIGNMENT LOGIC:
            # Create spaces equal to the length of the key (field name)
            end_spaces = len(key) * ' '
            
            # Add padding spaces to the value to align columns
            # This takes remaining spaces after the value length
            value += end_spaces[len(value):]
            
            # Print the padded value followed by pipe separator
            print(value, end='|')
        
        # Print newline after each user record (extra newline for spacing)
        print('\n')


def sort_users():
    """ Sort users alphabetically by last name
    
    Returns:
        list: Sorted list of user dictionaries
    """
    # Use sorted() with a lambda function to sort by 'last_name' key
    # The lambda extracts the last_name value from each dictionary
    return sorted(users, key=lambda k: k['last_name'])


if __name__ == "__main__":
    # Print the decorative header
    print_header()
    
    # Print the column headings
    print_headings()
    
    # Sort users by last name and update the users list
    users = sort_users()
    
    # Print all user records in formatted table
    print_users()