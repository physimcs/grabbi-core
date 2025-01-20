from transformers import pipeline

# Initialize the zero-shot classification pipeline
classifier = pipeline('zero-shot-classification', model='roberta-large-mnli')

# Text you want to classify
sequence_to_classify = "one day I will see the world"

# Candidate labels to classify against
candidate_labels = ['travel', 'cooking', 'dancing']

# Get classification results
result = classifier(sequence_to_classify, candidate_labels)

# Print the result
print(result)
