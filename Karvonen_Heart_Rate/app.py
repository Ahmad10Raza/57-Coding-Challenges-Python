# When you loop, you can control how much you increment
# the counter; you don’t always have to increment by one.
# When getting into a fitness program, you may want to figure
# out your target heart rate so you don’t overexert yourself.
# The Karvonen heart rate formula is one method you can use
# to determine your rate. Create a program that prompts for
# your age and your resting heart rate. Use the Karvonen for-
# mula to determine the target heart rate based on a range of
# intensities from 55% to 95%. Generate a table with the results
# as shown in the example output. The formula is
# TargetHeartRate = (((220 − age) − restingHR) × intensity) + restingHR
# Example Output
# Resting Pulse: 65
# Age: 22
# Intensity | Rate
# -------------|--------
# 55% | 138 bpm
# 60% | 145 bpm
# 65% | 151 bpm
# 70% | 157 bpm
# 75% | 164 bpm
# 80% | 170 bpm
# 85% | 178 bpm
# 90% | 185 bpm
# 95% | 191 bpm

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Karvonen Heart Rate \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)

def get_resting_heart_rate():
    while True:
        try:
            resting_heart_rate = input('Enter your resting heart rate: ')
            return int(resting_heart_rate)
        except ValueError:
            print('A valid input is required')

def get_age():
    while True:
        try:
            age = input('Enter your age: ')
            return int(age)
        except ValueError:
            print('A valid input is required')

def calculate_target_heart_rate(resting_heart_rate: int, age: int) -> int:
    """ Calculate the target heart rate """
    return (((220 - age) - resting_heart_rate) * 0.55) + resting_heart_rate


def print_target_heart_rate(target_heart_rate: int):
    print(f'Target Heart Rate: {target_heart_rate}')
    

if __name__ == '__main__':
    print_header()
    resting_heart_rate = get_resting_heart_rate()
    age = get_age()
    target_heart_rate = calculate_target_heart_rate(resting_heart_rate, age)
    print_target_heart_rate(target_heart_rate)
