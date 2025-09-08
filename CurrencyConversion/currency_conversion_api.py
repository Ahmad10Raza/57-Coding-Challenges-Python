import requests

class CurrencyConversion:
    rates = {}
    def __init__(self,url):
        data = requests.get(url).json()
        self.rates = data['rates']
        
        
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        
        if from_currency != 'EUR':
            amount = amount/self.rates[from_currency]
            
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        
        
if __name__ == "__main__":
    
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '7XXXXXXXXXXXXXXXXXXXX')
    
    CC = CurrencyConversion(url)
    from_country = input("From Country: ")
    to_country = input("To Country: ")
    amount = int(input("Amount: "))
    
    CC.convert(from_country, to_country, amount)