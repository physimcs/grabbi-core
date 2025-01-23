from sentence_transformers import SentenceTransformer, util

# Load a pre-trained RoBERTa model for sentence embeddings
model = SentenceTransformer('stsb-roberta-large')

article_1 = "Quantum mechanics is a fundamental theory in physics that describes nature at the smallest scales."
article_2 = "The study of quantum physics explores the behavior of particles at the atomic and subatomic levels."

# Generate embeddings for the articles
embedding_1 = model.encode(article_1, convert_to_tensor=True)
embedding_2 = model.encode(article_2, convert_to_tensor=True)

# Compute cosine similarity
cosine_similarity = util.cos_sim(embedding_1, embedding_2)

# Print similarity score
print(f"Semantic similarity: {cosine_similarity.item():.4f}")
