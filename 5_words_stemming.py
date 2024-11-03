import nltk 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

s="playing running dancing foxes grasses raining over the glass"

tokens=word_tokenize(s)
stem=[]
model=PorterStemmer()
for word in tokens:
    stem.append(model.stem(word))

print(stem)