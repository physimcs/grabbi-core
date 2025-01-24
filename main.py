from scraper import WikiScraper
from models import Models
from helper import HelperFunctions

"""scraper = WikiScraper()
internal_links = scraper.get_internal_links("https://en.wikipedia.org/wiki/Shark")
print(internal_links)"""

"""
model_instance = Models()

starting_article = "Artificial intelligence is the simulation of human intelligence in machines."
intended_article = "Machine learning is a subset of AI focused on statistical methods."

similarity_score = model_instance.model_pathfind(starting_article, intended_article)

print(f"Cosine Similarity: {similarity_score}")
"""

helper = HelperFunctions()

cut_link = helper.get_article_name("https://en.wikipedia.org/wiki/Shark")
cut_normalized_link = helper.normalize_article(cut_link)
print(cut_normalized_link)