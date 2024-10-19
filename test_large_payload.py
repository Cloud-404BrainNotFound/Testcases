# test_large_payload.py
import requests
from datetime import datetime, timezone

local = 1
if local:
    url = 'http://localhost:8004/orders/order_stringing'
else:
    url = 'http://54.237.161.55:8004/orders/order_stringing'

# Data with notes exceeding the 1000-character limit
large_notes_data = {
    "sport": "Tennis",
    "racket_model": "Wilson Pro Staff",
    "string": "Luxilon ALU Power",
    "tension": "55",
    "pickup_date": datetime.now(timezone.utc).isoformat(),
    "notes": "A" * 1001,  # 1001 characters, which should trigger the validation error
    "price": 20.00
}

# Sending the POST request with large notes
response = requests.post(url, json=large_notes_data)

# Check for validation error
if response.status_code == 422:
    print("Test passed: Validation error triggered for exceeding notes length.")
else:
    print(f"Test failed: Unexpected response status code {response.status_code}")