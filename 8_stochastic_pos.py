import nltk
from nltk.corpus import brown
from nltk.probability import ConditionalFreqDist, ConditionalProbDist, MLEProbDist
from nltk.tokenize import word_tokenize

# Ensure the necessary NLTK resources are downloaded
nltk.download('brown')
nltk.download('universal_tagset')

# Train a simple unigram POS tagger using the Brown corpus
def train_unigram_tagger():
    # Load the Brown corpus
    tagged_sents = brown.tagged_sents(tagset='universal')

    # Create a Conditional Frequency Distribution
    cfd = ConditionalFreqDist((word, tag) for sent in tagged_sents for (word, tag) in sent)
    
    # Create a Conditional Probability Distribution
    cpd = ConditionalProbDist(cfd, MLEProbDist)
    
    return cpd

# Tag words using the trained model
def stochastic_pos_tag(cpd, sentence):
    words = word_tokenize(sentence)
    tagged_sentence = []

    for word in words:
        # Get the most likely tag for the word
        if word in cpd:
            tag = cpd[word].max()
        else:
            # Default to 'NN' if the word is not in the training data
            tag = 'NN'
        tagged_sentence.append((word, tag))
    
    return tagged_sentence

# Train the model
cpd = train_unigram_tagger()

# Sample text
text = "NLTK is a powerful library for text processing and analysis in Python."

# Perform POS tagging using the stochastic tagger
tagged_text = stochastic_pos_tag(cpd, text)

# Display the tagged text
print(tagged_text)
