def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Numbers to Names \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)
    
    
def get_month_number():
    while True:
        try:
            month_num = input("Please Enter the Month's Numeric?: ")
            month_num = int(month_num)
            if month_num >=1 and month_num <= 12:
                return month_num
            else:
                print("A valid month's number required!")
        except ValueError:
            print("A valid month's number is required! ")
            
            
def get_month_from_number(month_number):

    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    
    return months.get(month_number,"Invalid Month's Number!")


def print_month(month):
    print(f'The name of the month is {month}')
    
    
def main():
    print_header()
    month_number = get_month_number()
    month = get_month_from_number(month_number)
    print_month(month)
    
if __name__ == '__main__':
    main()