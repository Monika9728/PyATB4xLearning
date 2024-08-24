number = int(input("Enter the number: "))
fact = 1
for i in range(1, number + 1):
    fact = fact * i
print("The factorial of", number, "is", fact)
if number < 0:
    print("The factorial of negative numbers doesn't exist")
elif number == 0:
    print("The factorial of 0 is 1")
