import random 


# Step 1: Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["car", "van", "lorry", "motorbike", "bus"]

# Step 2: Assign this list to a variable called word_list.
word_list = favorite_fruits

# Step 3: Generate a random word from the word_list.
word = random.choice(word_list)

# Step 4: Print out the newly created list to the standard output (screen).
print(word)

# Step 5: Ask the user to enter a single letter.
guess = input("Enter a single letter: ")

print(guess)