import requests
from bs4 import BeautifulSoup
import random

# Get Wiki links from Wiki page
def get_internal_links(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Exclude reference sections like 'reflist', 'reflist-columns', and 'references-column-width'
        refs = soup.find_all(class_='reflist reflist-columns references-column-width')
        for ref in refs:
            ref.decompose()

        # Exclude sections based on their headers because Wiki layout is weird
        sections_to_exclude = ['Further reading', 'External links']
        for header in soup.find_all(['span', 'h2']):
            if header.get_text().strip() in sections_to_exclude:
                # Remove the entire section if the header matches
                section = header.find_parent()
                if section:
                    section.decompose()

        # Find all links
        links = soup.find_all('a', href=True)

        internal_links = []
        for link in links:
            href = link['href']

            # Only include internal links starting with /wiki/ and exclude references or citations
            if href.startswith('/wiki/') and 'reference' not in href:
                internal_links.append('https://en.wikipedia.org' + href)

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
        print(f"Random link: {random_link}")
        new_links = get_internal_links(random_link)
    else:
        print("No random link selected.")
else:
    print("No internal links found.")