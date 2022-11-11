#%%
import random
# Computer chooses a random word from the word list
word_list = ['apple', 'grape', 'strawberry', 'mango', 'raspberry']
word = random.choice(word_list)

#%%
def check_guess(guess, word): # DOCSTRING?
    # check whether the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Please try again.")
        return False

def ask_for_input():
    # the user guesses single, alphabetic characters
    while True:
        letter_guess = input('Enter a single letter guess: ')
        # check if the guess is a single, alphabetic character
        if letter_guess.isalpha() and len(letter_guess) == 1:
            break
        else:
            print('Invalid letter. Please enter a single, alphabetic character.')
    if check_guess(letter_guess, word):
        # add to a list here
        return True
    else:
        ask_for_input()
#%%
