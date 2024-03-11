# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests, pathlib
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

body_content = soup.find('div', class_="col-sm-8 col-md-9")
l = body_content.find('ol', class_="row")
l = l.find_all('li')

for book in l:
    h3 = book.find('h3')
    a = h3.find('a')
    
    price = book.find('div', class_="product_price").find('p', class_="price_color").text

    print(f"Title: {a['title']}; price: {price}")
