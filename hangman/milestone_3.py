import random

# List of secret words
words = ["apple", "banana", "orange", "grape", "kiwi"]


def check_guess(guess):
    """
    Check if the guessed letter is in the randomly chosen secret word.

    Args:
        guess (str): The guessed letter.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()

    # Randomly choose a word from the list
    secret_word = random.choice(words)

    # Step 3: Move the code to check if the guess is in the word into this function block.
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
        return True
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        return False


def ask_for_input():
    """
    Continuously ask the user to guess a letter until a valid guess is made.
    """
    # Step 2: Define a function called ask_for_input.
    while True:
        # Step 2: Move the code to check if the guess is in the word into this function block.
        guess = input("Guess a letter: ")

        # Step 2: Move the code to check if the guess is in the word into this function block.
        if guess.isalpha() and len(guess) == 1:
            # Step 4: Outside the while loop, but within this function, call the check_guess
            # function to check if the guess is in the word.
            if check_guess(guess):
                break

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


# Step 4: Outside the function, call the ask_for_input function to test your code.
ask_for_input()
