import requests

url = "http://192.168.1.160:5000/login"
data = {"username": "lucy", "password": "123456"}
headers = {"Content-Type": "application/json"}

r = requests.post(url, json=data, headers=headers)

print(r.headers["Set-Cookie"])