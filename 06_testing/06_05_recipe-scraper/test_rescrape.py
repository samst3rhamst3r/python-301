# Write a unittest test suite to test the rescrape module

import unittest
import rescrape

class TestRescrape(unittest.TestCase):

    def setUp(self):
        self.base_url = rescrape.BASE_URL
    
    def test_get_page_content(self):
        content = rescrape.get_page_content(self.base_url)
        self.assertEqual(content.status_code, 200)

    def test_get_html_content(self):
        html = rescrape.get_html_content(self.base_url)
        self.assertIn("<!DOCTYPE html>", html)

    def test_make_soup(self):
        html = rescrape.get_html_content(self.base_url)
        soup = rescrape.make_soup(html)
        self.assertIsInstance(soup, rescrape.BeautifulSoup)

    def test_get_recipe_links(self):
        html = rescrape.get_html_content(self.base_url)
        soup = rescrape.make_soup(html)
        links = rescrape.get_recipe_links(soup)
        self.assertIn("recipes/", links[0])

    def test_get_author(self):
        html = rescrape.get_html_content(self.base_url)
        soup = rescrape.make_soup(html)
        links = rescrape.get_recipe_links(soup)

        recipe_html = rescrape.get_html_content(self.base_url + links[0])
        recipe_soup = rescrape.make_soup(recipe_html)

        author = rescrape.get_author(recipe_soup)
        self.assertIn("mrfish1991", author)

    def test_get_recipe(self):
        html = rescrape.get_html_content(self.base_url)
        soup = rescrape.make_soup(html)
        links = rescrape.get_recipe_links(soup)

        recipe_html = rescrape.get_html_content(self.base_url + links[0])
        recipe_soup = rescrape.make_soup(recipe_html)

        recipe_text = rescrape.get_recipe(recipe_soup)
        self.assertIn("like to receive a copy.\n", recipe_text)

if __name__ == "__main__":
    unittest.main()