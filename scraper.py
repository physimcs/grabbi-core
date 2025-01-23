import requests
from bs4 import BeautifulSoup
import random

class WikiScraper:
    def __init__(self):
        pass

    def is_valid_link(self, href):
        return (href.startswith('/wiki/') and
                'reference' not in href and
                not href.startswith('/wiki/Wikipedia:') and
                not href.startswith('/wiki/Special:') and
                not href.startswith('/wiki/Category:') and
                not href.startswith('/wiki/Talk:') and
                not href.startswith('/wiki/Help:'))

    def decompose_sections(self, soup, sections_to_exclude):
        for header in soup.find_all(['span', 'h2']):
            if header.get_text(strip=True) in sections_to_exclude:
                section = header.find_parent()
                if section:
                    section.decompose()

    def get_internal_links(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Exclude reference sections
            refs = soup.find_all(class_='reflist reflist-columns references-column-width')
            for ref in refs:
                ref.decompose()

            # Exclude sections based on headers
            self.decompose_sections(soup, ['Further reading', 'External links'])

            # Exclude links in specific header containers
            header_container = soup.find_all(class_='vector-header-container')
            for container in header_container:
                for link in container.find_all('a', href=True):
                    link.decompose()

            # Find all valid internal links
            links = soup.find_all('a', href=True)
            internal_links = [
                'https://en.wikipedia.org' + link['href']
                for link in links
                if self.is_valid_link(link['href'])
            ]

            return internal_links
        else:
            print(f"Error: Failed to retrieve {url}")
            return []