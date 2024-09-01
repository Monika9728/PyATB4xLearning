value = int(input("Enter a value limit: "))
a, b = 0, 1
print("The fibonacci series upto ", value, "is: ")
while a < value:
    print(a, end=" ")
    a, b = b, a + b
