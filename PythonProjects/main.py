import requests 
URL1 = 'https://api.pokemonbattle.ru/v2'
URL2 = 'https://lavka.pokemonbattle.ru'
TOKEN = '4b5ec406afcc43b211a9cb872ded3ce6'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN }

body_pokemon= {
    "name": "Holly",
    "photo_id": 7
}

body_rename = {
    "pokemon_id" : "275985",
    "name": "Lola",
    "photo_id": 7
}

body_pokeball = {
    "pokemon_id": "275985"
}

BODY_AV = {"order_type": "avatar","details": {"avatar_id": "2",
        "card_number": "4003600000000014", "card_name": "svetlana fed",
        "card_actual": "10/25", "card_cvv": "125", "secure_code": "56456"}}

'''response_pokemon = requests.post(url = f'{URL1}/pokemons', headers = HEADER, json = body_pokemon)
print(response_pokemon.text)'''

'''response_rename = requests.put(url=f'{URL1}/pokemons', headers=HEADER, json=body_rename)
print(response_rename.text)'''

'''response_pokeball = requests.post(url=f'{URL1}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response_pokeball.text)'''

response = requests.post(url = f'{URL2}/payments', headers = HEADER, json = BODY_AV)
print(response.text)

