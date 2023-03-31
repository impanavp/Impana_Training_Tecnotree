#7.Write a program that takes a list of numbers and returns a new list with only the prime numbers.

# Take input from the user
numbers = input("Enter a list of numbers: ").split()
# Convert each number in the list to an integer
numbers = [int(num) for num in numbers]

# Initialize an empty list to store the prime numbers
prime_numbers = []

# Loop through each number in the list
for num in numbers:
    # Check if the number is greater than 1
    if num > 1:
        # Loop through each number from 2 to the number itself
        for i in range(2, num):
            # Check if the number is divisible by any number other than 1 and itself
            if num % i == 0:
                # If it is, it is not a prime number, so break out of the loop
                break
        else:
            # If the loop completes without finding a divisor, the number is a prime number
            prime_numbers.append(num)

# Print the list of prime numbers
print("The prime numbers in the list are:", prime_numbers)
