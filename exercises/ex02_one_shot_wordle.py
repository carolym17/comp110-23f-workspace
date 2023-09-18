"""EX02 - My One Shot Wordle!"""

__author__ = "730477957" 

# Assigning the secret word

secret_word = "python"

# Assigning a variable to user's guessed word 

guess = str(input("What is your 6-letter guess? "))

# Adding named constants

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Establishing a variable to keep track of index and a variable to store emoji

tracking_index = 0
emoji = ""

# First checking if user guesses a word of the wrong length

while len(guess) != len(secret_word): 
    guess = (input(f"That was not {len(secret_word)} letters! Try again: "))
# Indicating if user has a right letter in correct spot or not 
while tracking_index < len(secret_word): 
    if guess[tracking_index] == secret_word[tracking_index]:
        emoji += GREEN_BOX
    else:
        letter_guess: bool = False
        a: int = 0
        while not (letter_guess) and a < len(secret_word):
            if secret_word[a] == guess[tracking_index]:
                letter_guess = True
            else: 
                a += 1
        if letter_guess: 
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX
    tracking_index += 1
  
# Telling the user if word is correct or not

print(emoji)
if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")
