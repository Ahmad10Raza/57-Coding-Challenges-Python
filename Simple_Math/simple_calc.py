def get_number():
  
    a = int(input("Enter First Number? "))    
    b = int(input("Enter First Number? "))
       
    return a,b

def add(a,b):
    return f'{a} + {b} = {a+b}'


def sub(a,b):
    return f'{a} - {b} = {a-b}'


def mul(a,b):
    return f'{a} * {b} = {a*b}'


def div(a,b):
    return f'{a} / {b} = {a/b}'

def main():
    a,b = get_number()
    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))
    print(div(a,b))
    
if __name__ == '__main__':
    main()