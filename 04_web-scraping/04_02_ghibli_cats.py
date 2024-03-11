# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.


import requests
from pprint import pprint

BASE_URL = "https://ghibliapi.vercel.app"
species_url = BASE_URL + "/species/"
people_url = BASE_URL + "/people/"
films_url = BASE_URL + "/films/"

cat_species = requests.get(species_url, params={"name": "Cat"}).json()[0]
cats = requests.get(people_url, params={"species": species_url + cat_species["id"]}).json()
films = requests.get(films_url).json()

films = {films_url + film["id"]: film for film in films}

cat_dict = {}
for cat in cats:
    
    cat.pop("id")
    cat.pop("species")
    cat.pop("url")

    cat["films"] = [films[film]["title"] for film in cat["films"]]

    pprint(cat)
