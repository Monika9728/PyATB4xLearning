number = float(input("Enter the number to be formatted: "))
formatted_number = f"{number:.2f}"
print("The formatted number is: ", formatted_number)

# format string
First_name = "Monika"
Second_name = "Chachinda"
print(f"My full name is: {First_name} {Second_name}")
# It works with single quotes too
print(f'My full name is: {First_name} {Second_name}')
# if I don't write f,The string will not be formatted
print("My full name is: {First_name} {Second_name}")

# alternatively
print("My full name is : ", First_name, Second_name)
