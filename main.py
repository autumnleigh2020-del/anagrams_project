"""
Project to find anagrams (single, then phrase, then game)
"""

import loaded_dictionary

word_list = loaded_dictionary.load('2of4brif.txt')
print(word_list)

# Create a list for anagrams
anagrams = []

# Ask user for a word
user_word = input("Enter a word: ").lower()

# Sort the user word
sorted_user_word = sorted(user_word)

# Loop through word list
for word in word_list:
  # Compare sorted words
  if sorted(word) == sorted_user_word and word != user_word:
    anagrams.append(word)

