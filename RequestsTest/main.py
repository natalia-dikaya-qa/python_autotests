import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '591ee4d6c4b4b64e838e4a1363a3f9c5'
HEADERS = {'Content-Type' : 'application/json',
           'trainer_token' : TOKEN}

body_create = {
    "name": "Питоняшка",
    "photo": "https://dolnikov.ru/pokemons/albums/099.png"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_create)

print(response_create.json())

body_rename = {
    "pokemon_id": "16324",
    "name": "Питончик"
}

response_rename = requests.patch(url=f'{URL}/pokemons', headers = HEADERS, json = body_rename)

print(response_rename.json())

body_pokeball = {
    "pokemon_id": "16324"
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball)

print(response_pokeball.json())