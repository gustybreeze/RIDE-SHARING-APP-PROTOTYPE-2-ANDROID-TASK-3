import requests

url = 'http://127.0.0.1:5000/request_ride'
data = {
    "user_id": 101,
    "source": "Noida",
    "destination": "Delhi"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
