num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))
if num1 > num2 and num1 > num3:
    print(f"The max number among 3 is: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"the max of 3 numbers is:{num2}")
else:
    print(f"The max of 3 no's is:{num3}")
