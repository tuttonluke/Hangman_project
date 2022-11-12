#%%
import random
# Computer chooses a random word from the word list
word_list = ['apple', 'grape', 'strawberry', 'mango', 'raspberry']
word = random.choice(word_list)

#%%
def check_guess(guess: str, word: str) -> bool:
    """Checks if letter guessed is contained in the word randomly chosen from
    the word list.

    Args:
        guess (str): single alphabetic character 
        word (str): word chosen randomly from word list

    Returns:
        bool: True if guess is correct, false if not.
    """    
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Please try again.")
        return False

def ask_for_input() -> bool:
    """Asks the user for input of a single, alphabetic character until a 
    valid input is given. It then calls the check_guess function which 
    checks if the inputed character is contained within the randomly selected 
    word from the word list.

    Returns:
        bool: True if guess is correct.
    """    
    while True:
        letter_guess = input('Enter a single letter guess: ')
        # check if the guess is a single, alphabetic character
        if letter_guess.isalpha() and len(letter_guess) == 1:
            break
        else:
            print('Invalid letter. Please enter a single, alphabetic character.')
    if check_guess(letter_guess, word):
        return True
    else:
        ask_for_input() # iterate until input is a correct guess
#%%
ask_for_input()
#%%
