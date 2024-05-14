import random 

def get_random_word(word_list):
    """
    Selects a random word from the given word list.
    """
    return random.choice(word_list)

def get_user_guess():
    """
    Prompts the user to enter a single letter and returns it.
    """
    return input("Enter a single letter: ")

def validate_guess(guess):
    """
    Validates the user's guess to ensure it is a single alphabetical character.
    """
    return len(guess) == 1 and guess.isalpha()

if __name__ == "__main__":

    # Step 1: Create a list containing the names of your 5 favorite fruits.
    vehicle = ["car", "van", "lorry", "motorbike", "bus"]

    # Step 2: Assign this list to a variable called word_list.
    word_list = vehicle

    # Step 3: Generate a random word from the word_list.
    word = random.choice(word_list)

    # Step 4: Print out the newly created list to the standard output (screen).
    print(word)

    # Step 5: Ask the user to enter a single letter.
    guess = get_user_guess()
    if validate_guess(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
