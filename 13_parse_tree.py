import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

# Define a simple grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> DT N | 'John'
    VP -> V NP 
    DT -> 'the' | 'a'
    N -> 'dog' | 'park'
    V -> 'saw' | 'walked'
""")

# Define a simple sentence
sentence = "John saw the dog".split()

# Create a parser
parser = RecursiveDescentParser(grammar)

# Generate and print the parse trees
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
