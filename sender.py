import requests

url = "http://127.0.0.1:5080/send"

data = {"message": "Hello",
        "vector": 600000}
response = requests.post(url, json=data)
print(response)
