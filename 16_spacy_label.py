#pip install spacy
#python -m spacy download en_core_web_sm

import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Define a sample text
text = "Apple is looking at buying U.K. startup for $1 billion.  Elon Musk is the CEO of Tesla Inc., and he lives in California."

# Process the text
doc = nlp(text)

# Extract named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
