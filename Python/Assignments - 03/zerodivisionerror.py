# Python program that takes two numbers as input from the user and performs division.
#Handle the ZeroDivisionError exception and prompt the user to enter a non-zero denominator.

# While loop untill user enter the valid number
while True:
    try:
        # Enter the numerator and denominator
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        # Check if the denominator is non-zero and the numerator is greater than the denominator
        if denominator != 0 and numerator >= denominator and numerator > 0 :
            # Perform division and print the result
            result = numerator / denominator
            print(f"The result of {numerator}/{denominator} is {result}")
            break  # Exit the loop if the input is valid
        else:
            # Prompt the user to enter valid input
            if numerator <= 0:
                print("Error: Numerator should be greater than 0.")
            elif denominator == 0:
                print("Error: Denominator cannot be zero.")
            else:
                print("Error: Numerator should be greater than the denominator.")
    except ValueError:
        # Handle the exception if the input is not a number
        print("Error: Please enter a valid number for numerator and denominator.")
