import requests


BASE = "http://127.0.0.1:5000/"


response = requests.put(BASE + "travel/1", {"rating": 10, "city": "London", "restaurant": "McDonalds"})
print(response.json())
input()

response = requests.get(BASE + "travel/1")
print(response.json())