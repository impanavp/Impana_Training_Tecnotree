
#9.Write a program that takes a list of numbers and returns a new list with the elements squared.

# take input from user
lst = input("Enter a list of numbers: ").split()

# convert string elements to integers
lst = [int(i) for i in lst]

# create a new list with squared elements
squared_lst = [num**2 for num in lst]

# print the squared list
print("The squared list is:", squared_lst)
