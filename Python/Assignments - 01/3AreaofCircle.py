# 3.Write a program that asks the user to enter a radius, and then calculates and prints out the area and circumference of a circle with that radius.
# The formulas for calculating the area and circumference of a circle are A = pi * r^2 and C = 2 * pi * r, where pi is a constant value of approximately 3.14.

import math

# Input for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print("The area of the circle is: {:.4f}".format(area))
print("The circumference of the circle is: {:.4f}".format(circumference))
