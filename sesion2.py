import requests

URL = 'https://pokeapi.co/api/v2/pokemon/ditto'

response = requests.get(URL)
print(response.status_code)
print(response)