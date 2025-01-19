from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set up the driver with webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Shark Wikipedia article
driver.get("https://en.wikipedia.org/wiki/Shark")

# Wait for an element to load (for example, the title of the page)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstHeading")))

# The browser will remain open until you press Enter in the terminal
input("Press Enter to close the browser...")

# Close the driver after pressing Enter
driver.quit()
