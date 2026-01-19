import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
json_data = response.json()

print("Status code:", response.status_code)
print("Joke ID:", json_data["id"])
print("Joke:")
print(json_data["value"])
