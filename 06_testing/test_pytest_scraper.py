
import x06_06_pytest_scraper as scraper

BASE_URL = "https://ghibliapi.vercel.app"
species_url = BASE_URL + "/species/"
people_url = BASE_URL + "/people/"
films_url = BASE_URL + "/films/"

def test_get_cat_species():
    species = scraper.get_cat_species(species_url)
    assert species["name"] == "Cat"

def test_get_cats():
    cats = scraper.get_cats(people_url, species_url)
    assert len(cats) > 0

def test_get_films():
    films = scraper.get_films(films_url)
    assert len(films) > 0

def test_get_cat_info():
    cats = scraper.get_cat_info(species_url, people_url, films_url)
    assert len(cats) > 0
