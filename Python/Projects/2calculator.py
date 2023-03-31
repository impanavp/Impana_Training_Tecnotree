# Calculator: Build a simple calculator that allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division.
# You can use Python's input() function to take user input and print() function to display the result.

# Define a function for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Ask the user to input two numbers and the operation they want to perform
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+,-,*,/): ")

# Check the operator and perform the corresponding arithmetic operation
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    print("Invalid operator.")

# Display the result to the user
print("Result:", result)
