import sys

import loaded_dictionary
from collections import Counter


dictionary = loaded_dictionary.load('2of4brif.txt')
dictionary.append('a')
dictionary.append('l')
dictionary = sorted(dictionary)

user_name = input("Enter your name:")

def find_anagrams (name, word_list):
    """Read name and dictionary file and display all anagrams in name"""
    nlm = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        wlm = Counter(word.lower())
        for letter in word:
            if wlm [letter] < nlm[letter]:
                test += letter
            if Counter (test) == wlm:
                anagrams.append(word)

    print(*anagrams, sep = "\n")
    print()
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining real world anagrams = {len(word_list)}")


def process_choice (name):
    """Check user choice for validity, return choice and leftover letters."""
    while True:
        choice = input('\nMake a choice else Enter to start over or # to end: ')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Wrong! Make another choice!", file=sys.stderr)
        name = ''.join(left_over_list) # makes display more readable
        return choice, name


def main():
    """Build anagram phrase from user's name"""
    name = ''.join(user_name.lower().split())
    name = name.replace('-', '')

    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ','')
        if len(temp_phrase) < limit:
            print("Length of anagram phrase = {}".format(len(temp_phrase)))
            find_anagrams(name, dictionary)
            print("Current anagram phrase =", end= " ")
            choice, name = process_choice(name)
            phrase += choice + ' '
        elif len(temp_phrase) == limit:
            print("\n*****FINISHED*****\n")
            print("Anagram of name =", end=" ")
            print(phrase, file=sys.stderr)
            print()
            try_again = input('\n\nTry again? (Press Enter else "n" to quit)\n ')
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()


