import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define a probabilistic context-free grammar (PCFG)
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [1.0]
    V -> "eats" [1.0]
    NP -> "John" [0.5] | Det N [0.5]
    Det -> "a" [1.0]
    N -> "cake" [1.0]
""")

# Create a parser using the PCFG
parser = ViterbiParser(grammar)

# Define a sentence to parse
sentence = "John eats a cake".split()

# Parse the sentence
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
