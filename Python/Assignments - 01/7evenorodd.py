# 7.Write a program that asks the user to enter a number and then prints out whether it is even or odd.

# Ask user for a number
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
