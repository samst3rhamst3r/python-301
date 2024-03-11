# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

import unittest
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

class TestGhibliCats(unittest.TestCase):

    def setUp(self):
        BASE_URL = "https://ghibliapi.vercel.app"
        self.species_url = BASE_URL + "/species/"
        self.people_url = BASE_URL + "/people/"
        self.films_url = BASE_URL + "/films/"
    
    def test_get_cat_species(self):
        species = get_cat_species(self.species_url)
        self.assertEqual(species["name"], "Cat")
    
    def test_get_cats(self):
        cats = get_cats(self.people_url, self.species_url)
        self.assertGreater(len(cats), 0)
    
    def test_get_films(self):
        films = get_films(self.films_url)
        self.assertGreater(len(films), 0)
    
    def test_get_cat_info(self):
        cats = get_cat_info(self.species_url, self.people_url, self.films_url)
        self.assertGreater(len(cats), 0)

if __name__ == "__main__":
    unittest.main()
