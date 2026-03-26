"""
Project to find anagrams (single, then phrase, then game)
"""

import loaded_dictionary

# Load dictionary file
word_list = loaded_dictionary.load('2of4brif.txt')
print(word_list)

# Create a list for anagrams
anagrams = []

# Ask user for a word
user_word = input("Enter word: ").lower()
sorted_user_word = sorted(user_word)

# Loop through word list
for word in word_list:
  # Compare each to sorted version
  if sorted(word) == sorted(user_word) and word != user_word:
    anagrams.append(word)

# Point all anagrams with a # of anagrams.

print(f"\nTotal number of anagrams: {len(anagrams)}")