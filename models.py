from sentence_transformers import SentenceTransformer, util

class Models:
    def __init__(self, model_name='stsb-roberta-large'):
        self.model = SentenceTransformer(model_name)

    def model_pathfind(self, starting_article, intended_article):
        # Encode both articles
        embedded_starting_article = self.model.encode(starting_article)
        embedded_intended_article = self.model.encode(intended_article)

        # Compute cosine similarity
        cosine_similarity = util.cos_sim(embedded_starting_article, embedded_intended_article)

        # Return the similarity score
        return cosine_similarity.item()
