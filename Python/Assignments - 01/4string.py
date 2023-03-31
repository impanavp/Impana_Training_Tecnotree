# 4.Write a program that asks the user to enter a string and then prints out the length of the string,
# the first and last characters, and the string in reverse order.

# Ask user for string
string = input("Enter a string: ")

# Calculate length of string
length = len(string)

# Get first and last characters
first_char = string[0]
last_char = string[-1]

# Reverse the string
reversed_string = string[::-1]

# Print the results
print("Length of string: ", length)
print("First character: ", first_char)
print("Last character: ", last_char)
print("String in reverse order: ", reversed_string)
