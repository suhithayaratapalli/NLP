import re

# Define a simple corpus
corpus = [
    "The quick brown fox jumps over the lazy dog",
    "John loves Mary",
    "I am learning Python"
]

# Define transformation rules
transformation_rules = [
    (r'^[Tt]he$', 'DT'),
    (r'^[Aa]m$', 'VB'),
    (r'^[Ll]oves$', 'VB'),
    (r'^[Jj]ohn$', 'NNP'),  # Proper Noun (John)
    (r'^[Mm]ary$', 'NNP'),  # Proper Noun (Mary)
    (r'^[Pp]ython$', 'NNP')
]

tagged_sentences = []

# Process each sentence in the corpus
for s in corpus:
    # Process each word in the sentence
    for w in s.split():
        tagged = False
        # Apply each transformation rule
        for pattern, tag in transformation_rules:
            if re.match(pattern, w):
                tagged_sentences.append((w, tag))
                tagged = True
                break
        # If no rule matched, tag as 'NN'
        if not tagged:
            tagged_sentences.append((w, 'NN'))

# Print the tagged sentences
print(tagged_sentences)
