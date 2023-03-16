import math
import string

# Define a function to count letters in a string


def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count

# Define a function to count words in a string


def count_words(text):
    count = 1  # account for the first word
    for char in text:
        if char.isspace():
            count += 1
    return count

# Define a function to count sentences in a string


def count_sentences(text):
    count = 0
    for char in text:
        if char in ['.', '!', '?']:
            count += 1
    return count


# Get input text from user
text = input("Text: ")

# Count letters, words, and sentences
letter_count = count_letters(text)
word_count = count_words(text)
sentence_count = count_sentences(text)

# Calculate Coleman-Liau index
L = (letter_count / word_count) * 100
S = (sentence_count / word_count) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# Print grade level
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
