# Hangman: introductory project of the AiCore curriculum.

The project is an implementation of the classic hangman game, where the computer selects a word at random from a list of words, and the user attempts to guess it.

To play the game, run the play_game function in the file [play_hangman.py](https://github.com/tuttonluke/aicore_hangman_project/blob/master/project_files/play_hangman.py), passing in a list of words as an argument, from which one will be randomly chosen for the user to guess.

# Project Documentation

This introductory project in the AiCore curriculum introduces core concepts such as version control, object oriented programming,
and programming good practice by the implementation of the classic game of hangman.

## Milestone 1
Technologies / Skills:
- Command line (Bash and Command Prompt)
- Git
- GitHub

Gained familiarity with navigating the command line and the use of Git for version control and GitHub for web hosting.

## Milestone 2
Technologies / Skills:
- VSCode
- Markdown
- Python data types

## Milestone 3
Technologies / Skills:
- Python functions
- Comments, docstrings, and typing.

The ask_for_input function asks the user for input of a single, alphabetic character until a valid input is given. It then calls the check_guess function which checks if the inputed character is contained within the randomly selected word from the word list.

## Milestone 4
Technologies / Skills:
- Object Oriented Programming

Implements ask_for_input and check_guess as methods in the Hangman class.

## Milestone 5

Defines a function called play_game to insantiate and instance of the Hangman class and run the game as expected.