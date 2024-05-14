"""
Milestone 5: Hangman Game

This module implements a simple Hangman game where the player guesses letters to
reveal a hidden word. 
The game randomly selects a word from a predefined list and allows the player a
limited number of attempts to guess the word correctly.

Classes:
--------
Hangman:
    A class representing the Hangman game. It initializes the game with a random
    word from a list and manages the game state.

Functions:
---------
play_game(word_list):
    A function to play the Hangman game. It initializes the game and handles the
    game logic until the player wins or loses.

Usage:
------
1. Ensure the `milestone_4.py` module containing the Hangman class is in the same
directory as this script.
2. Run the script using Python:
    ```
    python milestone_5.py
    ```

3. Follow the on-screen instructions to play the Hangman game.
"""

from milestone_4 import Hangman


def play_game(word_list):
    """
    Play the Hangman game.

    Parameters:
    -----------
    word_list : list
        A list of words to be used in the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "grape", "kiwi"]
    play_game(word_list)
