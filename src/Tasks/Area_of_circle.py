# Write a Python program to calculate the area of a circle
# given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

import math

radius = float(input("Enter a radius: "))
pi = 3.14
area_of_circle = pi * radius * radius
print(f"The area of the circle with radius {radius} is: {area_of_circle:.2f}")

# or another method
area_of_circle = math.pi * math.pow(radius, 2)
print(f"The area of the circle with radius {radius} is: {area_of_circle:.2f}")

# another method
area_of_circle = pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {area_of_circle:.2f}")
