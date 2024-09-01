def print_arguments(*args):  # *args is a list
    # *args = multiple number of arguments with no limit, -> List
    # print (args[0]) # printing the string on 0th index of *args list

    for i in args:
        print(i, end=" ")  # can be used to print everything via loop


print_arguments("A", "B", "C")
print_arguments("it", "was", "a", "LOVELY", "Weather")
print_arguments(1, True)  # ANYTHING (datatype) CAN BE PASSED

print("Hello")
print("Hello", "User")
print("Hello", "User", 123)
print("Hello", "User", 123, "Welcome")
print("Hello", "User", 123, "Welcome", True)
