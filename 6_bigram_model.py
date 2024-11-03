import nltk
from collections import defaultdict, Counter
from nltk.tokenize import word_tokenize

# Sample text
text = "The quick brown fox jumps over the lazy dog. The dog barks at the fox. The fox runs away."

# Tokenize the text
tokens = word_tokenize(text)

# Create bigrams
bigrams = list(nltk.bigrams(tokens))
print(bigrams)
# Build the bigram model
bigram_model = defaultdict(Counter)
print(bigram_model)
for w1, w2 in bigrams:
    bigram_model[w1][w2] += 1
print(bigram_model)
# Function to generate text using the bigram model without randomness
def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word]
    for _ in range(num_words - 1):
        if current_word in bigram_model:
            # Choose the most frequent next word
            next_word = bigram_model[current_word].most_common(1)[0][0]
            result.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(result)

# Generate text starting with 'The'
generated_text = generate_text('The', 15)
print("Generated Text:", generated_text)
