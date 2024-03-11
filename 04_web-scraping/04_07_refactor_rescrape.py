# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests, pathlib
from bs4 import BeautifulSoup

def get_page(url):
    return BeautifulSoup(requests.get(url).text, features="html.parser")

def get_titles_and_prices(li_tags):
    
    l = []
    for book in li_tags:
        h3 = book.find('h3')
        a = h3.find('a')
        
        price = book.find('div', class_="product_price").find('p', class_="price_color").text
        l.append((a['title'], price))
    
    return l

url = "http://books.toscrape.com"

soup = get_page(url)

body_content = soup.find('div', class_="col-sm-8 col-md-9")
l = body_content.find('ol', class_="row")
l = l.find_all('li')

print(get_titles_and_prices(l))

