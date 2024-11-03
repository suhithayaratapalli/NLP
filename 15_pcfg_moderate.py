import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define a probabilistic context-free grammar (PCFG)
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.6] | V NP PP [0.4]
    PP -> P NP [1.0]
    V -> "saw" [0.5] | "ate" [0.5]
    NP -> "John" [0.2] | "Mary" [0.3] | "Bob" [0.3] | Det N [0.2]
    Det -> "a" [0.5] | "an" [0.5]
    N -> "dog" [0.4] | "cat" [0.6]
    P -> "with" [1.0]
""")

# Create a parser using the PCFG
parser = ViterbiParser(grammar)

# Define a sentence to parse
sentence = "John saw a dog with Mary".split()

# Parse the sentence
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
