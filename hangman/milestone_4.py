"""
Hangman Module

This module implements a simple Hangman game where the player guesses letters to reveal
a hidden word. 
The game randomly selects a word from a predefined list and allows the player a limited
number of attempts to guess the word correctly.

Classes:
--------
Hangman:
    A class representing the Hangman game. It initializes the game with a random word from
    a list and manages the game state.

Usage:
------
1. Create an instance of the Hangman class with a list of words:
    game = Hangman(word_list)

2. Call the ask_for_input method to prompt the player for a letter:
    game.ask_for_input()

3. Repeat step 2 until the player guesses the word or runs out of lives.

4. Play the game!
"""

import random


class Hangman:
    """
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.


    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_',
        '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    """

    def __init__(self, word_list:list, num_lives:int=5)->None:
        """
        Initialize the Hangman game.

        Parameters:
        ----------
        word_list: list
            List of words to be used in the game
        num_lives: int, optional
            Number of lives the player has (default is 5)
        """
        self._word_list = word_list
        self.num_lives = num_lives
        self._word = random.choice(self._word_list)
        self._word_guessed = ["_" for _ in self._word]
        self.num_letters = len(set(self._word))
        self._guessed_letters = []
        print(f"The mystery word has {self.num_letters} characters")
        print(self._word_guessed)

    def _update_word_guessed(self, guess:str)->None:
        """
        Updates the word_guessed list with the guessed letter.

        Parameters:
        ----------
        guess: str
            The letter guessed by the player
        """
        for i, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[i] = guess
        self.num_letters -= 1

    def _update_num_lives(self):
        """
        Updates the number of lives when a wrong guess is made.
        """

        self.num_lives -= 1

    def check_guess(self, guess:str)->None:
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.

        Parameters:
        ----------
        guess: str
            The letter guessed by the player
        """
        guess = guess.lower()
        if guess in self._word:
            print(f"Good guess! '{guess}' is in the word.")
            self._update_word_guessed(guess)

        else:
            self._update_num_lives()
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self)->None:
        """
        Asks the user for a letter and checks if it's valid, then calls check_guess method.
        """

        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self._guessed_letters:
                print("You already tried that letter!")
                continue
            else:
                self.check_guess(guess)
                self._guessed_letters.append(guess)
                break


if __name__ == "__main__":
    # Testing the Hangman class
    hangman_game = Hangman(["apple", "banana", "orange", "grape", "kiwi"])
    hangman_game.ask_for_input()
