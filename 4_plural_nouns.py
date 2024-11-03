import nltk
from nltk import pos_tag, word_tokenize

# Download the 'punkt' resource if it hasn't been downloaded yet
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
words = word_tokenize(sentence)
print(words)

# Tag parts of speech
tags = pos_tag(words)
print(tags)

# Extract nouns and pluralize them if necessary
nouns = []
for word, pos in tags:
    if pos.startswith("NN"):
        nouns.append(word)

print(nouns)
if nouns:
    for noun in nouns:
        if noun[-1].lower() in {'s', 'x', 'z'} or noun[-2:].lower() in {'ch', 'sh'}:
            print(noun + 'es')
        else:
            print(noun + 's')
else:
    print("No nouns found")
