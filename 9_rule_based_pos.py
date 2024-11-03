import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Ensure the necessary NLTK resources are downloaded
nltk.download('punkt')

# Define a list of (regexp, tag) patterns
patterns = [
    (r'.*ing$', 'VBG'),  # gerunds
    (r'.*ed$', 'VBD'),   # past tense verbs
    (r'.*es$', 'VBZ'),   # 3rd person singular present verbs
    (r'.*ould$', 'MD'),  # modals
    (r'.*\'s$', 'POS'),  # possessive nouns
    (r'.*s$', 'NNS'),    # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')        # nouns (default)
]

# Create a RegexpTagger with the defined patterns
regexp_tagger = RegexpTagger(patterns)

def rule_based_pos_tag(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform POS tagging using the RegexpTagger
    tagged_words = regexp_tagger.tag(words)
    
    return tagged_words

# Sample text
text = "John's running towards the new markets could be surprising."

# Perform POS tagging using the rule-based tagger
tagged_text = rule_based_pos_tag(text)

# Display the tagged text
print(tagged_text)
