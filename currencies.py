import requests

list_currencies = []

host = 'api.frankfurter.app'

# Mengambil data daftar mata uang dari endpoint API
response = requests.get(f'https://{host}/currencies')

currencies = response.json()

# Memasukan data daftar mata uang dari json ke bentuk list
for key, value in currencies.items():
    str_curr = f'{key} - {value}'
    list_currencies.append(str_curr)









