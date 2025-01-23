import requests
from bs4 import BeautifulSoup
import random

class WikiScraper:
    def __init__(self):
        pass

    # Move click_link above get_random_link
    def click_link(url):
        response = requests.get(url)

        if response.status_code == 200:
            return response.url
        else:
            return f"Error {response.status_code}"

    # Get Wiki links from Wiki page
    def get_internal_links(url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Exclude reference sections
            refs = soup.find_all(class_='reflist reflist-columns references-column-width')
            for ref in refs:
                ref.decompose()

            # Exclude sections based on headers
            sections_to_exclude = ['Further reading', 'External links']
            for header in soup.find_all(['span', 'h2']):
                if header.get_text(strip=True) in sections_to_exclude:
                    section = header.find_parent()
                    if section:
                        section.decompose()

            # Find all internal links
            links = soup.find_all('a', href=True)
            internal_links = [
                'https://en.wikipedia.org' + link['href']
                for link in links
                if link['href'].startswith('/wiki/') and 'reference' not in link['href']
            ]

            print(f"Found {len(internal_links)} internal links.")
            return internal_links
        else:
            print(f"Error: Failed to retrieve {url}")
            return []

    # Get random link by clicking Wiki random
    def get_random_link():
        url = "https://en.wikipedia.org/wiki/Special:Random"
        return WikiScraper.click_link(url)