# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import webbrowser

class Ingredient:

    def __init__(self, name: str, amount: int) -> None:
        self.name = name
        self.amount = amount
    
    def get_info(base_url):
        url 