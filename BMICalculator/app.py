def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' BMI Calculator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)
    
def get_weight():
    while True:
        try:
            age = input('What is your weight(In Pounds)? ')
            return float(age)
        except ValueError:
            print('a valid input required')
            
def get_height():
    while True:
        try:
            age = input('What is your height(In Inches)? ')
            return float(age)
        except ValueError:
            print('a valid input required')
            
def bmi_calc(weight,height):
    bmi = (weight/(height**2)*703)
    return round(bmi,2)

def print_bmi(bmi):
    print(f'Your BMI is {bmi}')

def main():
    height = get_height()
    weight = get_weight()
    bmi = bmi_calc(weight,height)
    print_bmi(bmi)
    if bmi >= 18.5 and bmi <= 25:
        
        print("You are within the ideal weight range.")
    else:
       
        print("You are overweight. You should see your doctor.")
        
        
if __name__ == '__main__':
    main()