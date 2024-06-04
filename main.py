import requests

def currency_converter():
    initial_currency = input('Enter the initial currency: ')
    target_currency = input('Enter the target currency: ')

    while True:
        try:
            amount = float(input('Enter the amount: '))
        except:
            print('The amount needs to be numeric')
            continue

        if not amount>0: 
            print('Amount needs to be greater than 0')
        else: 
            break

    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "0QtaZuejfqWHlYHGWO0ZYUcOwsun2CBr"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code

    if status_code != 200:
        result = response.json()
        print('Error Response: ' + str(result))
        quit()

    result = response.json()
    print('Conversion Result: ' + str(result['result']))

if __name__ == '__main__':
    currency_converter()

# Currency Symbols
'''url = "http://api.apilayer.com/fixer/symbols"

payload = {}
headers= {
  "apikey": "0QtaZuejfqWHlYHGWO0ZYUcOwsun2CBr"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

result = response.json()
print('Result: ' + str(result))
'''
