import requests
from bs4 import BeautifulSoup
import random

# Get Wiki links from Wiki page
def get_internal_links(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        internal_links = [
            'https://en.wikipedia.org' + link['href'] for link in links
            if link['href'].startswith('/wiki/')
        ]
        print(f"Found {len(internal_links)} internal links.")
        return internal_links
    else:
        print(f"Error: Failed to retrieve {url}")
        return []

# Temp function to select a random link from the list of links
def get_random_link(links):
    return random.choice(links) if links else None

internal_links = get_internal_links("https://en.wikipedia.org/wiki/Shark")
if internal_links:
    random_link = get_random_link(internal_links)
    if random_link:
        print(f"Random link: {random_link}")  # Print the randomly selected link
        new_links = get_internal_links(random_link)
    else:
        print("No random link selected.")
else:
    print("No internal links found.")