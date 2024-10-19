import requests
from datetime import datetime, timezone

local = 1
if local:
    url = 'http://localhost:8004/orders/order_stringing'
else:
    url = 'http://54.237.161.55:8004/orders/order_stringing'
    
# Data for a valid stringing order
data = {
    "sport": "Tennis",
    "racket_model": "Wilson Pro Staff",
    "string": "Luxilon ALU Power",
    "tension": "55",  # String tension
    "pickup_date": datetime.now(timezone.utc).isoformat(),  # Current time in ISO format
    "notes": "Please string at 55 lbs",
    "price": 20.00  # Price for stringing
}

# Sending the POST request to add a new stringing order
response = requests.post(url, json=data)

# Validate response
if response.status_code == 201:
    print("Test passed: Order created successfully.")
else:
    print("Test failed: Unexpected response status code", response.status_code)

# Print the response body
print(response.json())

