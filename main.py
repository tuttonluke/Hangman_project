#%%
import random

word_list = ['apple', 'grape', 'strawberry', 'mango', 'raspberry']
print(word_list)
# choose a word at random from the list of words
word = random.choice(word_list)
print(word)
# %%
# Assign user input to variable 'guess',
guess = input('Enter a single letter: ')
# check the user input is a single alphabetic character.
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
