import requests
from bs4 import BeautifulSoup
import random
import urllib.parse

# Get Wiki links
def get_internal_links(url):
    # Send get request to url
    response = requests.get(url)

    # Check if response is successful
    if response.status_code == 200:
        # Parse content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links
        links = soup.find_all('a', href = True)
        # Filter links to only be Wiki links
        internal_links = [
            'https://en.wikipedia.org' + link['href'] for link in links 
            if link['href'].startswith('/wiki/')
        ]
        
        return internal_links
    else:
        # Error handling
        print(f'Error: Failed to retrieve {url}' )
        return []
    
url = 'https://en.wikipedia.org/wiki/Shark'
internal_links = get_internal_links(url)
print(internal_links)