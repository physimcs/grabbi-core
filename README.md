# ML Wiki Game
The Wiki Game is a game where a player starts on a randomly selected article on Wikipedia and must navigate through internal Wikipedia links to reach a randomly selected endpoint article.

This project aims to leverage machine learning and natural language processing (NLP), going beyond traditional pathfinding methods, to optimize the Wikipedia navigation process. By incorporating semantic understanding of the articles and their content, the system will intelligently choose the best links to click and navigate through, ultimately reaching the endpoint article faster.

This is more of an exercise in 'can it be done' rather than 'is it the most efficient way to do it'.

# Progress
This project is a work in progress, but here are some of the key achievements so far:
* Web Scraping: Implemented a combination of BeautifulSoup and Selenium to scrape internal links from Wikipedia articles. BeautifulSoup is used to parse the HTML and extract all internal links, while Selenium is used to click on the links (like one would in the real Wikipedia game).
