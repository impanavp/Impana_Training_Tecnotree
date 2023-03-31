# 8.Write a program that asks the user to enter a list of names and then prints out the names in alphabetical order.

name_list = input("Enter a list of names separated by spaces: ").split()

# Iterate through the list of names and compare each pair of adjacent names
for i in range(len(name_list)-1):
    for j in range(i+1, len(name_list)):
        # If the current name comes after the next name in alphabetical order, swap them
        if name_list[i] > name_list[j]:
            name_list[i], name_list[j] = name_list[j], name_list[i]

# Print the sorted list of names
print("Sorted names:")
for name in name_list:
    print(name)

