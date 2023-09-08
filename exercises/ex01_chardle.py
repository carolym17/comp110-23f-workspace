"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730477957"

guessed_word = str(input("Enter a 5-character word: "))

if len(guessed_word) != 5:
    print("Word must contain 5 characters")
    exit()

guessed_letter = str(input("Enter a single character: "))

if len(guessed_letter) != 1:
    print("Character must be a single character.")
    exit()

print("Searching for " + guessed_letter + " in " + guessed_word)

matches = 0

if guessed_letter == guessed_word[0]: 
    print(guessed_letter + " found at index 0")
    matches = matches + 1

if guessed_letter == guessed_word[1]: 
    print(guessed_letter + " found at index 1")
    matches = matches + 1

if guessed_letter == guessed_word[2]: 
    print(guessed_letter + " found at index 2")
    matches = matches + 1

if guessed_letter == guessed_word[3]: 
    print(guessed_letter + " found at index 3")
    matches = matches + 1

if guessed_letter == guessed_word[4]: 
    print(guessed_letter + " found at index 4")
    matches = matches + 1
 
if matches == 1:
    print(str(matches) + " instance of " + guessed_letter + " found in " + guessed_word)

if matches > 1:
    print(str(matches) + " instances of " + guessed_letter + " found in " + guessed_word)

if matches < 1:
    print("No instances of " + guessed_letter + " found in " + guessed_word)