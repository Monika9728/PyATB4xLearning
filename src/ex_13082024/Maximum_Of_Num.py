first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
third_number = float(input("Enter third number: "))
# By max function

# print((max(first_number, second_number, third_number)))

# By If statement
if (first_number > second_number) and (first_number > third_number):
    print("The greater number is: ", first_number)
elif (second_number > first_number) and (second_number > third_number):
    print("The greater number is: ", second_number)
elif (third_number > first_number) and (third_number > second_number):
    print("The greater number is: ", third_number)
