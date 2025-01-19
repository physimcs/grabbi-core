import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set up the driver with webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
        return internal_links
    else:
        print(f"Error: Failed to retrieve {url}")
        return []

# Temp function to select a random link from the list of links
def get_random_link(links):
    return random.choice(links) if links else None  # Return a random link, or None if list is empty

def open_new_link(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstHeading")))
    input("Press Enter to close the browser...")  # Keeps the browser open until you press Enter
    driver.quit()

# Get internal links from the specified Wikipedia page
internal_links = get_internal_links("https://en.wikipedia.org/wiki/Shark")

if internal_links:
    random_link = get_random_link(internal_links)
    open_new_link(random_link)
    print(random_link)
else:
    print("No internal links found.")
