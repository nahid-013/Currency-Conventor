import requests

API_KEY =  "7e0d971cd8c1de510fb11b16"
def get_dans(from_currency, to_currency):
    data = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}')
    return round(float(data.json()['conversion_rates'][to_currency]), 2)
    # print(round(float(data.json()['conversion_rates'][to_currency]), 2))

# get_dans('USD','RUB')



