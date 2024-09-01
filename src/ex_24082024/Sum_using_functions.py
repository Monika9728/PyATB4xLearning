num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))


def sum_of_three_numbers(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_numbers(num1, num2, num3)
addition = sum_of_three_numbers(n1=num1, n2=num2,n3=num3) #line 10,line 11 both r same
result = sum_of_three_numbers(num1, num2, num3)
print(result)
print(addition)
