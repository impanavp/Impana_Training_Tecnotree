# Hangman Game: Develop a text-based game where the user must guess a secret word by guessing one letter at a time.
# You can use a predefined list of words and randomly select one of them using Python's random module.

import random

# Define a list of words to choose from
words = ["apple", "banana", "cherry", "orange", "pear"]

# Select a random word from the list
word = random.choice(words)

# Create an empty list to store the correct guesses
correct_guesses = []

# Create a variable to track the number of incorrect guesses
incorrect_guesses = 0

# Create a list of characters for the Hangman image
hangman = ["  O", " /|\\", " / \\", "___"]

# Define a function to display the Hangman image
def display_hangman():
    print("\n".join(hangman[:incorrect_guesses]))

# Define a function to display the current state of the word
def display_word():
    for letter in word:
        if letter in correct_guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

# Loop until the player wins or loses
while True:
    # Display the Hangman image and the current state of the word
    display_hangman()
    display_word()
    
    # Ask the player to guess a letter
    guess = input("Guess a letter: ")
    
    # Check if the guess is correct
    if guess in word:
        correct_guesses.append(guess)
    else:
        incorrect_guesses += 1
        
    # Check if the player has won or lost
    if all(letter in correct_guesses for letter in word):
        print("Congratulations! You won!")
        break
    elif incorrect_guesses == len(hangman):
        print("Sorry, you lost. The word was", word)
        break
