import requests
from datetime import datetime

local = 0
if local:
    url = 'http://localhost:8004/orders/order_stringing'
else:
    url = 'http://54.237.161.55:8004/orders/order_stringing'

# Data to test the /order_stringing endpoint
data = {
    "sport": "Tennis",
    "racket_model": "Wilson Pro Staff",
    "string": "Luxilon ALU Power",
    "tension": "55",  # String tension
    "pickup_date": datetime.utcnow().isoformat(),  # Current time in ISO format
    "notes": "Please string at 55 lbs",
    "price": 20.00  # Price for stringing
}

# Sending the POST request to add a new stringing order
response = requests.post(url, json=data)

# Printing out the status code and response
print(response.status_code)
print(response.json())

# Additional tests for validation errors or variations
# For example, missing required fields
# invalid_data = {
#     "sport": "Tennis",
#     "racket_model": "",  # Invalid, missing racket model
#     "string": "Luxilon ALU Power",
#     "tension": "55",
#     "pickup_date": datetime.utcnow().isoformat(),
#     "price": 20.00
# }

# response = requests.post(url, json=invalid_data)
# print("Invalid data status code:", response.status_code)
# print("Invalid data response:", response.json())