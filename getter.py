import requests

url = "http://127.0.0.1:5080/get/1"

data = requests.get(url)

print(data.json())
