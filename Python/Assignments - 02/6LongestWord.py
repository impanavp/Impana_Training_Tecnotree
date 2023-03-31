# 6.Write a program that takes a list of words and returns the longest word in the list.

# Take input from the user
words = input("Enter a list of words: ").split()

# Initialize a variable to store the longest word
longest_word = ""

# Loop through each word in the list
for word in words:
    # Check if the current word is longer than the longest word found so far
    if len(word) >= len(longest_word):
        # If it is, update the longest_word variable
        longest_word = word

# Print the longest word
print("The longest word in the list is:", longest_word)
