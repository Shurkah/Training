import json
import requests

url = "https://api.chucknorris.io/jokes/random"
joke = requests.get(url)

jk = json.loads(joke.text)

print(jk['value'])