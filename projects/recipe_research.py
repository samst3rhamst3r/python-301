# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import requests, pathlib
from bs4 import BeautifulSoup
from pprint import pprint

if __name__ == "__main__":

    BASE_URL = "https://codingnomads.github.io/recipes/"

    print("Welcome to the recipe reviewer!")

    ingredients = []
    while True:

        print("Please choose from the following options:")
        print("1. Input ingredient(s)")
        print("2. Clear ingredients list")
        print("3. Execute search for recipes (must have min 1 ingredient input)")
        print("4. QUIT")

        choice = input()
        match choice:
            case "1":
                print("Please input a list of ingredients as a comma-separated list")
                ingredients.extend(ingredient.strip() for ingredient in input().split(","))
            case "2":
                ingredients.clear()
            case "3":
                path_list = []
                for file in pathlib.Path(__file__).parent / "webpages":
                    with open(file, 'r') as f:
                        path_list.append(BASE_URL + file)
                        for ingredient in ingredients:
                            if ingredient not in f.read():
                                path_list.pop()
                                break
                        
                
            case "4":
                break
            case _:
                print("Invalid. Please input valid option.")
    
    print("Thank you for using the recipe review tool!")


content = requests.get(BASE_URL)

soup = BeautifulSoup(content.text, features="html.parser")
links = soup.find_all('a')

for link in links:
    href = link['href']
    file_name = href.split("recipes/")[1]
    content = requests.get(BASE_URL + href)
    with open(pathlib.Path(__file__).parent / "webpages" / file_name, 'w') as f:
        f.write(content.text)