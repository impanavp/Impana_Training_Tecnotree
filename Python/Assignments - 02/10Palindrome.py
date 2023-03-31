#10.Write a program that takes a list of strings and returns a new list with only the strings that are palindromes.

# take input from user
lst = input("Enter a list of strings: ").split()

# create a new list with palindromic strings
palindrome_lst = [word for word in lst if word == word[::-1]]

# print the palindrome list
print("The palindromes in the list are:", palindrome_lst)
