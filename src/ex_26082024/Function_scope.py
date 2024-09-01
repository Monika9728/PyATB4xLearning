global_num = 12


def my_function():
    age = 10
    print(age)  # scope of variable within function
    print(global_num)


# print(age)  # throws an error
my_function()
print(global_num) #accessible as it is global variable