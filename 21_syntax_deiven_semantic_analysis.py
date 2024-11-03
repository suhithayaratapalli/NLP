import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract noun phrases and their meanings
def extract_noun_phrases_meanings(sentence):
    doc = nlp(sentence)
    
    noun_phrases = []
    for np in doc.noun_chunks:
        # Get the noun phrase
        noun_phrase = np.text
        
        # Get the meaning of the noun phrase (in this case, the definition from WordNet)
        # Here, we just assume the noun phrase itself is the meaning for simplicity
        meaning = noun_phrase
        
        noun_phrases.append((noun_phrase, meaning))
    
    return noun_phrases

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Extract noun phrases and their meanings
noun_phrases_meanings = extract_noun_phrases_meanings(sentence)

# Print the results
for noun_phrase, meaning in noun_phrases_meanings:
    print(f"Noun Phrase: {noun_phrase}, Meaning: {meaning}")
