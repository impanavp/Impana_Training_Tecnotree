#8.Write a program that takes a string and returns the number of times each letter appears in the string.

# Take input from the user
string = input("Enter a string: ")

# Initialize an empty dictionary to store the letter counts
letter_counts = {}

# Loop through each character in the string
for char in string:
    # Check if the character is a letter
    if char.isalpha():
        # If it is, convert it to lowercase
        char = char.lower()
        # Check if the character is already in the dictionary
        if char in letter_counts:
            # If it is, increment its count
            letter_counts[char] += 1
        else:
            # If it is not, add it to the dictionary with a count of 1
            letter_counts[char] = 1

# Print the letter counts
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
