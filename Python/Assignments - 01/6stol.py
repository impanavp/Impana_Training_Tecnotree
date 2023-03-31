# 6.Write a program that asks the user to enter a list of numbers and then prints out the largest and smallest numbers in the list.

num_list = input("Enter a list of numbers separated by spaces: ").split()

# Initialize the largest and smallest numbers
largest_num = int(num_list[0])
smallest_num = int(num_list[0])

# Iterate through the list of numbers and update the largest and smallest numbers
for num in num_list:
    num = int(num)
    if num > largest_num:
        largest_num = num
    if num < smallest_num:
        smallest_num = num

# Print the largest and smallest numbers
print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
