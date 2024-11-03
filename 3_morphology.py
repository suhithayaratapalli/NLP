from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import PorterStemmer

# Sample sentence
s = "raining hanging Running and played are both verb forms of the word run and play."

# Tokenize the sentence
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(s)
print(tokens)

# Perform stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(token) for token in tokens]
print(stemmed_words)
