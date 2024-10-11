# Function to count occurrences of specified words in the text
def count_words(text, words_to_count):
    word_count = {word: 0 for word in words_to_count}  # Initialize dictionary with zero counts
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
    return word_count

# Read the content of the text file (update the path according to your file location)
with open('E:/AdvancedPython/AdvPython/john_text/book of John text.txt', 'r') as file:
    text = file.read()

# List of words to count (case sensitive, including lowercase 'spirit')
words_to_count = ['Father', 'God', 'Christ', 'Spirit', 'spirit', 'life', 'man']

# Get the word count
word_count = count_words(text, words_to_count)

# Display the word counts (without single quotes or additional text)
for word, count in word_count.items():
    print(f"{word}: {count}")
