# test_invalid_data_type.py
import requests
from datetime import datetime

local = 1
if local:
    url = 'http://localhost:8004/orders/order_stringing'
else:
    url = 'http://54.237.161.55:8004/orders/order_stringing'

# Data with invalid price type (should be a float, not a string)
invalid_data = {
    "sport": "Tennis",
    "racket_model": "Wilson Pro Staff",
    "string": "Luxilon ALU Power",
    "tension": "55",
    "pickup_date": datetime.utcnow().isoformat(),
    "notes": "Please string at 55 lbs",
    "price": "twenty"  # Invalid price (should be a float)
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
