#1.Write a program that takes a list of numbers and returns the sum of all even numbers in the list.

# Take input from user
numbers = input("Enter a list of numbers: ").split(" ")

# Convert input into a list of integers
numbers = [int(num) for num in numbers]

# Initialize sum and count variables to 0
sum_of_even = 0
count = 0

# Loop through each number in the list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Add the number to the sum
        sum_of_even += num
        count += 1

# Print the sum of all even numbers
print("Count of even numbers: ", count)
print("Sum of all even numbers in the list: ", sum_of_even)
