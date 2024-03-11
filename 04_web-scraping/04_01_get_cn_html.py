# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!
import requests
from pprint import pprint
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.com"
page = requests.get(BASE_URL)
pprint(page.text)