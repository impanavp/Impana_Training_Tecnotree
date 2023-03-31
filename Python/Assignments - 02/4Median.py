# 4.Write a program that takes a list of numbers and returns the median value.

# Take input from user
numbers = input("Enter a list of numbers: ").split(" ")

# Convert input into a list of integers
numbers = [int(num) for num in numbers]

# Sort the list of numbers in ascending order
numbers.sort()

# Find the middle index of the list
middle_index = len(numbers) // 2

# Check if the length of the list is odd
if len(numbers) % 2 == 1:
    # If the length of the list is odd, the median is the middle number
    median = numbers[middle_index]
else:
    # If the length of the list is even, the median is the average of the two middle numbers
    median = (numbers[middle_index - 1] + numbers[middle_index]) / 2

# Print the median value of the list
print("Median value of the list:", median)
