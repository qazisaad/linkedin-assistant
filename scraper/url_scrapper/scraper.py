from model import Page
<<<<<<< HEAD

=======
from utils import fetch_page
import requests
from bs4 import BeautifulSoup
import pandas as pd
>>>>>>> 811984543ea00f10cf031fc93a131b26af4539bc
class Scraper:
    def __init__(self, url):
        self.url = url
    
    def scrape(self):

        # Parse the page HTML and create a Page object
        page = Page(self.url)
        page.parse()

        # Return the Page object
        return page
