import pytest 
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4b5ec406afcc43b211a9cb872ded3ce6'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = "27040"

body_pokemon= {
    "name": "Holly",
    "photo_id": 7
}

def test_status_code1():
    response_spisok= requests.get(url=f'{URL}/pokemons', params={"trainer_id":TRAINER_ID})
    assert response_spisok.status_code == 200

def test_status_code2():
    response_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon)
    assert response_pokemon.status_code == 201

def test_part (): 
    response_part = requests.get(url=f'{URL}/pokemons', params={"trainer_id":TRAINER_ID})
    assert response_part.json()["data"][0]["name"] == 'Lola'

def test_in_pokeball (): 
    response_in_pokeball = requests.get(url=f'{URL}/pokemons', params={"in_pokeball":1})
    assert response_in_pokeball.json()["data"][0]["in_pokeball"] == 1
