#%%
from milestone_5 import Hangman
word_list = ['apple', 'grape', 'strawberry', 'mango', 'raspberry']

def play_game(word_list: list) -> str:
    """This function creates an instance of the Hangman class and plays the game.

    Args:
        word_list (list): list of words from which to play the hangman game.
    """    
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            print(game.word_guessed, '\n')
        else:
            print('Congratulations, you won the game!')
            break
#%%
play_game(word_list)