#%%
word_list = ['apple', 'grape', 'strawberry', 'mango', 'raspberry']
#%%
import random

class Hangman:
    """
    This class is an implementation of the classic hangman game, where the computer 
    thinks of a word and the user attempts to guess it.

    Attributes:
        word_list (list): list of words from which the computer randomly chooses one.
        num_lives (int): number of lives left
        word (list): characters of the word to be guessed in a list.
        word_guessed (list): current state of the guessed word.
        num_letters (int): number of unique letters in self.word that have not been 
            guessed yet.
        list_of_guesses (list): list of guessed letters.
    """    
    def __init__(self, word_list: list, num_lives=5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = list(random.choice(word_list)) # word to be guessed as a list
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word).difference(self.word_guessed))
        self.list_of_guesses = [] # list of guesses already tried
    
    def check_guess(self, guess: str) -> bool:
        """Checks if letter guessed is contained in the word randomly chosen from
        the word list.

        Args:
            guess (str): single alphabetic character.

        Returns:
            bool: True if guess is correct, false if not.
        """        
        guess = guess.lower()
        if guess in self.word: # if guess is correct
            print(f"Good guess! {guess} is in the word.")
            # modify self.word_guessed to include correctly guessed letters
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            return True
        else:
            print(f"Sorry, {guess} is not in the word. Please try again.")
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives remaining.')
            return False
    
    def ask_for_input(self) -> bool:
        """Asks the user for input of a single, alphabetic character until a 
        valid input is given. It then calls the check_guess function which 
        checks if the inputed character is contained within the randomly selected 
        word from the word list.

        Returns:
            bool: True if guess is correct, False otherwise.
        """
        while True:
            letter_guess = input('Enter a single letter guess: ')
            # check if the guess is a single, alphabetic character
            if not (letter_guess.isalpha() and len(letter_guess) == 1):
                print('Invalid letter. Please enter a single, alphabetic character.')
                break
                # self.ask_for_input()
            # check if the guess has already been made
            elif letter_guess in self.list_of_guesses:
                print('You already tried that letter!')
                break
            else:
                self.list_of_guesses.append(letter_guess)
                # return True if letter_guess is in self.word, False otherwise.
                return self.check_guess(letter_guess) 
                

my_hangman = Hangman(word_list)
#%%
