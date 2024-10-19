# test_missing_required_field.py
import requests
from datetime import datetime

local = 1
if local:
    url = 'http://localhost:8004/orders/order_stringing'
else:
    url = 'http://54.237.161.55:8004/orders/order_stringing'

# Data with missing required fields
invalid_data = {
    "sport": "Tennis",
    "racket_model": "",  # Missing racket model
    "string": "Luxilon ALU Power",
    "tension": "55",
    "pickup_date": datetime.utcnow().isoformat()
    # "price": 20.00
}

# Sending the POST request with invalid data
response = requests.post(url, json=invalid_data)

# Validate response
if response.status_code == 422:  # Expecting a validation error
    print("Test passed: Validation error returned as expected.")
else:
    print("Test failed: Unexpected response status code", response.status_code)

# Print the response body
print(response.json())
