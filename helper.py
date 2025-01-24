
class HelperFunctions:
    def __init__(self):
        pass

    def get_article_name(self,url):
        return url.removeprefix('https://en.wikipedia.org/wiki/')
    
    def normalize_article(self,url):
        return url.lower().strip()