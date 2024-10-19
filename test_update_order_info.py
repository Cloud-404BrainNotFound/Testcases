import requests

local = 1
if local:
    url = 'http://localhost:8004/orders/orders'
else:
    url = 'http://54.237.161.55:8004/orders/orders'

# Test updating order information
order_id = "254a696f-ce24-4d6c-a8dd-99ae712fd35a"  # Replace with a valid order ID from your data
# Test updating order information with a successful case
successful_data = {
    "string": "New String Type",
    "tension": "60"  # Valid data for tension
}

# Sending the PUT request for a successful update
response = requests.put(f"{url}/{order_id}", json=successful_data)

# Check for a successful update (200 OK)
if response.status_code == 200:
    print("Test passed: Order info updated successfully.")
else:
    print(f"Test failed: Unexpected response status code {response.status_code}")
print(response.json())

data = {
    "string": "New String Type",
    "tension": "5"  # This should trigger an error due to invalid data
}

response = requests.put(f"{url}/{order_id}", json=data)

# Check for validation error
if response.status_code == 400:
    print("Test passed: Validation error triggered successfully.")
else:
    print("Test failed: Unexpected response status code", response.status_code)

# Print the response body
print(response.json())


