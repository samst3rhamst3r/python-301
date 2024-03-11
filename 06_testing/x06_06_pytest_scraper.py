# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

import requests

def get_cat_species(species_url):
    return requests.get(species_url, params={"name": "Cat"}).json()[0]

def get_cats(people_url, species_url):
    cat_species = get_cat_species(species_url)
    return requests.get(people_url, params={"species": species_url + cat_species["id"]}).json()

def get_films(films_url):
    films = requests.get(films_url).json()
    return {films_url + film["id"]: film for film in films}

def get_cat_info(species_url, people_url, films_url):
    cats_list = get_cats(people_url, species_url)
    films_dict = get_films(films_url)
    for cat in cats_list:
        
        cat.pop("id")
        cat.pop("species")
        cat.pop("url")

        cat["films"] = [films_dict[film]["title"] for film in cat["films"]]
    
    return cats_list

