# 2.Write a program that asks the user to enter a temperature in Celsius, and then converts it to Fahrenheit and prints out the result.
# The formula for converting Celsius to Fahrenheit is F = (C * 9/5) + 32.
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
