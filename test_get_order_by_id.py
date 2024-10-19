import requests

local = 1
if local:
    url = 'http://localhost:8004/orders/orders'
else:
    url = 'http://54.237.161.55:8004/orders/orders'

# Test retrieving an order by ID
order_id = "254a696f-ce24-4d6c-a8dd-99ae712fd35a"  # Replace with a valid order ID from your data
print(f"URL being hit: {url}/{order_id}")
response = requests.get(f"{url}/{order_id}")

# Validate response
if response.status_code == 200:
    print("Test passed: Order retrieved successfully.")
else:
    print("Test failed: Unexpected response status code", response.status_code)

# Print the response body
print(response.json())
