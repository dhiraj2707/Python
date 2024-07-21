import requests
jokes_api = "https://v2.jokeapi.dev/joke/Dark"

response = requests.get(jokes_api)

print(response.json()["joke"])