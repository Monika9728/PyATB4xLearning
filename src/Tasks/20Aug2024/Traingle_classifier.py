# ### Task #8
#
# ✅ Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1 = int(input("First side: "))
side2 = int(input("Second side: "))
side3 = int(input("Third side: "))

if side1 == side2 == side3:
    print("This is Equilateral Triangle")
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("This is a Scalene Triangle")
else:
    print("This is an isosceles Triangle")
