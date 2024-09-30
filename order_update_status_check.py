import requests

url = 'http://localhost:8000/orders/update_order_status'
local = 0
if local:
    url = 'http://localhost:8000/orders/update_order_status'
else:
    url = 'http://34.203.249.254:8004/orders/update_order_status'


data = {
    "order_id": "73c57a9f-8349-4f25-941c-3b7e89e4c0e5",
    "status": "shipped"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())