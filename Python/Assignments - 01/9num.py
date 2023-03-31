# 9.	Write a program that asks the user to enter a number and then prints out all the numbers from 1 to that number.

# Ask user for a number
num = int(input("Enter a number: "))

# Print all the numbers from 1 to num
print("Numbers from 1 to", num, ":")
for i in range(1, num+1):
    print(i)
