import requests
import json

while True:
    pokemonSearch = input("What is the species of pokemon you would like information on? ")

    pokemonSearch = pokemonSearch.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonSearch}"

    req = requests.get(url)
    if req.status_code == 200:
        pokemonData = req.json()

        print(f"Name is \t\t {pokemonData['name']}")
        print(f"Abilities:")
        for ability in pokemonData['abilities']:
            print(ability['ability']['name'])
        print(f"Pokedex id is \t\t {pokemonData['id']}")
        for move in pokemonData['moves']:
            print(move['move']['name'])
    else:
        print("Pokemon not found")