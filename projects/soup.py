import webbrowser, sys

class Ingredient:

    def __init__(self, name: str, amount: int) -> None:
        for c in name:
            if not c.isalpha() and not c.isspace():
                name = name.replace(c, " ")
        self.name = " ".join(name.strip().lower().split())
        self.amount = amount
    
    def get_info(self, base_url):
        
        url_name = self.name.capitalize().replace(" ", "_")

        url = base_url + url_name

        try:
            webbrowser.open_new_tab(url)
        except webbrowser.Error:
            print("Could not open browser tab. Please check browser", file=sys.stderr)

    def __str__(self):
        return f"{self.name.capitalize()}: {self.amount}"

if __name__ == "__main__":

    base_url = "https://en.wikipedia.org/wiki/"

    tomato = Ingredient(". _ tomato &", 5)
    tomato.get_info(base_url)