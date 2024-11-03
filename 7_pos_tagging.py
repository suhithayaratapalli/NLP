import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Ensure the necessary NLTK resources are downloaded


def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    return tagged_words

# Sample text
text = "NLTK is a powerful library for text processing and analysis in Python."

# Perform POS tagging
tagged_text = pos_tagging(text)

# Display the tagged text
print(tagged_text)
