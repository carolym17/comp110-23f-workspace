"""EX03 - My Structured Wordle!"""

__author__ = "730477957"

# Emoji for if guess letter is not in secret 
WHITE_BOX: str = "\U00002B1C"  
# Emoji for guess letters that match secret at the same position
GREEN_BOX: str = "\U0001F7E9"  
# Emoji for if letter in guess is in secret but in a different position
YELLOW_BOX: str = "\U0001F7E8"  


# Declaring function to check the length and if any characters match at the correct indices
def contains_char(secret: str, letter: str) -> bool: 
    """Checks length and if character match at any indices of secret!"""
    assert len(letter) == 1
    i = 0
    found = False
    while i < len(secret): 
        if letter == secret[i]:
            found = True 
        i += 1
    return found


# Declaring fucntion return the string of emojis 
def emojified(guess: str, secret: str) -> str:
    """Checks to add the correct emoji!"""
    assert len(guess) == len(secret)
    emoji: str = ""
    a = 0
    while a < len(secret): 
        if guess[a] == secret[a]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[a]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        a += 1
    return emoji


# Declaring fucntion to prompt the user to guess a word of the correct length
def input_guess(expected_length: int) -> str: 
    """Prompts the user for a guess and continues to prompt until guess is correct length."""
    guess = (input(f"Enter a {(expected_length)} character word: "))
    while expected_length != len(guess): 
       guess = (input(f"That wasn't {(expected_length)} chars! Try again: "))
    return guess


# Declaring main fucntion to implement the main Wodle game
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"
    number_of_turns = 6
    won_the_game = False 
# Prints the current turn the user is on
    while number_of_turns > 0 and won_the_game == False:
        print(f"=== Turn {(6 - number_of_turns + 1)}/6 ===")
# Prompt the user for a guess 
        guess: str = input_guess(len(secret_word))
# Codify the emoji results of the user's guess 
        add_emoji: str = emojified(guess, secret_word)
# Prints the emoji string 
        print(add_emoji)
# If the user guesses the correct word
        if guess == secret_word:
            won_the_game = True 
# Tracks the number of tries if the user does not guess the correct word 
        else:
            number_of_turns = number_of_turns - 1
# If the user won, it indicates to the user that they won the game
    if won_the_game == True: 
        print(f"You won in {(6 - number_of_turns + 1)}/6 turns!")
# If the user did not guess the correct word in six or less tries  
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__": 
    main()
    