# - Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or
# equal to the second number.

input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))
if input1 > input2:
    print(input1, "is greater than", input2)
elif input1 < input2:
    print(input1, "is less than", input2)
else:
    print("First number is equal to second number")
