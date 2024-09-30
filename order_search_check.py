import requests

order_id = '73c57a9f-8349-4f25-941c-3b7e89e4c0e5'

local = 0
if local:
    url = f'http://localhost:8000/orders/get_order/{order_id}'
else:
    url = f'http://34.203.249.254:8004/orders/get_order/{order_id}'


response = requests.get(url)
print(response.status_code)
print(response.json())