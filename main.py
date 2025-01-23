from scraper import WikiScraper

internal_links = WikiScraper.get_internal_links("https://en.wikipedia.org/wiki/Comparison_of_programming_languages#General_comparison")
print(internal_links)