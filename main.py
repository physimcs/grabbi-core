from scraper import WikiScraper

scraper = WikiScraper()
internal_links = scraper.get_internal_links("https://en.wikipedia.org/wiki/Shark")
print(internal_links)