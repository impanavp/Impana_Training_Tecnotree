# 2.Write a program that takes a string and returns a new string with all the vowels removed.

# Take input from user
string = input("Enter a string: ")

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Initialize a new string without vowels
new_string = ""

# Loop through each character in the string
for char in string:
    # Check if the character is not a vowel
    if char not in vowels:
        # Add the character to the new string
        new_string += char

# Print the new string without vowels
print("String without vowels:", new_string)
