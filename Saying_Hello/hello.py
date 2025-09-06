# def hello(name):
#     return f"Hello {name}, nice to meet you!"


# name = input("What is your name? ")
# print(hello(name))


def print_header():
    """ Print header """
    header_text = ''
    TEXT = f' Saying Hello \n'
    LINE = '-' * len(TEXT)
    LINE += '\n'

    header_text += LINE
    header_text += TEXT
    header_text += LINE
    print(header_text)
    

def get_name():
    while True:
        name = input("What is you name? ")
        
        if len(name) >= 3:
            return name
        

def greet(name):
    print(f"Hello {name}, nice to meet you!")
    
def main():
    print_header()
    name = get_name()
    greet(name)
    
if __name__ == '__main__':
    main()