import requests

url = 'http://54.83.149.21:8002/payments/add_payment'
local = 0
if local:
    url = 'http://localhost:8002/payments/add_payment'
else:
    url = 'http://54.237.161.55:8002/payments/add_payment'
data = {
    "card_number": "4111111111111111",
    "expiry_month": "12",
    "expiry_year": "25",
    "cvc": "123",
    "status": "PENDING"  # Status is an enum: "PENDING", "COMPLETED", "FAILED"
}
response = requests.post(url, json=data)
print(response.text)

data = {
    "card_number": "4222222222222222",
    "expiry_month": "11",
    "expiry_year": "24",
    "cvc": "456",
    "status": "COMPLETED"
}
response = requests.post(url, json=data)
print(response.text)

data = {
    "card_number": "4333333333333333",
    "expiry_month": "10",
    "expiry_year": "23",
    "cvc": "789",
    "status": "FAILED"
}

response = requests.post(url, json=data)
print(response.text)


