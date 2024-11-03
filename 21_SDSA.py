import spacy

nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases(sentence):
    # Process the sentence with spaCy
    doc = nlp(sentence)
    noun_phrases = []
    for chunk in doc.noun_chunks:
        np_text = chunk.text
        np_head = chunk.root.head.text
        noun_phrases.append((np_text, np_head))

    return noun_phrases

sentence = "The quick brown fox jumps over the lazy dog in the park."
noun_phrases = extract_noun_phrases(sentence)

print("Noun Phrases and their Meanings:")
for np, meaning in noun_phrases:
    print(f"Noun Phrase: '{np}' - Meaning: '{meaning}'")
