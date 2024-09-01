import math

a = lambda a, b, c: a + b + c
print(a(1, 2, 3))

even_odd = lambda num: "Even" if num % 2 == 0 else "odd"
print(even_odd(5))

number=int(input("enter a number: "))
powered_number=lambda num:num**3
print(powered_number(number))
op=lambda :math.pow(int(input("number: ")),2)
print(op())
