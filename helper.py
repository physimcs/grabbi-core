class HelperFunctions:
    def __init__(self):
        pass

    def get_article_name(self,url):
        return url.removeprefix('https://en.wikipedia.org/wiki/')
    
    def normalize_article(self,url):
        # Wikipedia articles use underscores as spaces in urls, here we change it back to spaces
        if "_" in url:
            url = url.replace("_", " ")
        return url.lower().strip()
    
    def link_name_pair(self,links):
        # Initialize dictionary
        paired_links = {}

        # For each link, normalize and cut
        for link in links:
            normalized_link = self.normalize_article(link)
            new_link = self.get_article_name(normalized_link)
            paired_links[new_link] = link
        
        # return article names and links
        return paired_links