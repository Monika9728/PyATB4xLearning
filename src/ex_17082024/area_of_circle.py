import math

pi = 3.14
radius = float(input("Enter the radius: "))
area_of_circle = math.pi * math.pow(radius, 2)
print("The area of circle : ", area_of_circle)
print(f"The area of circle :  {area_of_circle:.2f}") #upto 2 digits

# print(3.14*float(input("Enter the radius: "))**2")