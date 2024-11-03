import spacy

nlp = spacy.load("en_core_web_sm")

def calculate_sentence_similarity(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    print(sentences)
    if len(sentences) < 2:
        return 0.0
    
    total_similarity = 0.0
    count = 0
    
    for i in range(len(sentences) - 1):
        sent1 = sentences[i]
        sent2 = sentences[i + 1]
        similarity = sent1.similarity(sent2)
        total_similarity += similarity
        count += 1
    
    average_similarity = total_similarity / count
    return average_similarity

# Example text
text = ("Alice went to the market. She bought some apples. Later, she went home and cooked dinner.")

# Calculate and print the coherence score
coherence_score = calculate_sentence_similarity(text)
print(f"Coherence Score: {coherence_score:.2f}")
