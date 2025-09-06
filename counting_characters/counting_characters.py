def print_header():
    """ Print header """
    header_text = ''
    TEXT = f' Couting Chracter \n'
    LINE = '-' * len(TEXT)
    LINE += '\n'

    header_text += LINE
    header_text += TEXT
    header_text += LINE
    print(header_text)
    
def get_string():
    while True:
        str = input("What is the input string? ")
        if len(str) > 0:
            return str    
        print("A valid input string required!")

def print_length(str):
    print(f'{str} has {len(str)} chracter')
    
    
def main():
    print_header()
    str = get_string()
    print_length(str)
    
if __name__ == '__main__':
    main()