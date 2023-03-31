# 10.	Write a program that asks the user to enter a list of numbers and then prints out the sum of all the even numbers in the list.

# Ask user for a list of numbers
num_list = input("Enter a list of numbers, separated by spaces: ")

# Convert the string of numbers into a list of integers
num_list = num_list.split()
num_list = [int(num) for num in num_list]

# Calculate the sum of all even numbers in the list
even_sum = sum(num for num in num_list if num % 2 == 0)

# Print the result
print("Sum of all even numbers in the list:", even_sum)
