# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests
from pprint import pprint

BASE_URL = "https://pokeapi.co/api/v2/"

pokemon_api = BASE_URL + "pokemon/"

# 20 results are returned as a paginated response. I'll just use 6 of those
pokemones = requests.get(pokemon_api).json()["results"]

for i in range(6):
    pokemon = pokemones[i * 3]
    pokemon = requests.get(pokemon["url"]).json()
    species = requests.get(pokemon['species']['url']).json()
    
    print()
    print(f"Name: {pokemon['name']}")
    print(f"\tNumber: {pokemon['id']}")
    print(f"\tType: {species['egg_groups']}")