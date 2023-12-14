import requests

list_currencies = []

host = 'api.frankfurter.app'

# Get currencies list from API
response = requests.get(f'https://{host}/currencies')

currencies = response.json()

# Turn json file to list
for key, value in currencies.items():
    str_curr = f'{key} - {value}'
    list_currencies.append(str_curr)









