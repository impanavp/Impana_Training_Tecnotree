#5.Write a program that takes two lists of numbers and returns a new list with the elements that appear in both lists.

# Take input from user
list1 = input("Enter the first list of numbers: ").split(" ")
list2 = input("Enter the second list of numbers: ").split(" ")

# Convert input into lists of integers
list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

# Initialize a new list for common elements
common_elements = []

# Loop through each element in the first list
for num in list1:
    # Check if the element is in the second list
    if num in list2:
        # Add the element to the list of common elements
        common_elements.append(num)

# Print the list of common elements
print("List of common elements:", common_elements)
