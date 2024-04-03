#проверить ответ GET/trainers на код 200
#проверить, что в ответе есть имя моего тренера (поиск с квери trainer_id)

import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '591ee4d6c4b4b64e838e4a1363a3f9c5'
HEADERS = {'Content-Type' : 'application/json',
           'trainer_token' : TOKEN}

def test_status_code():
    response  = requests.get(url = f'{URL}/trainers', params = {"trainer_id":2387})
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id":2387})
    assert response.json()['data'][0]['trainer_name'] == 'Tasha'