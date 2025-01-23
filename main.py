from scraper import WikiScraper

internal_links = WikiScraper.get_internal_links("https://en.wikipedia.org/wiki/Shark")
print(internal_links)