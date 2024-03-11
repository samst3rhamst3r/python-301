# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import requests, pathlib
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Web_scraping"

content = requests.get(URL)
soup = BeautifulSoup(content.text, features="html.parser")

body_content = soup.find("div", class_="mw-body-content")

links = body_content.find_all("a")
links_list = []
for link in links:
    if "https" in link['href']:
        links_list.append(link['href'])

next_page = requests.get(links_list[0])
with open(pathlib.Path(__file__).parent / "04_05_wiki_scrape.html", 'w') as f:
    f.write(next_page.text)