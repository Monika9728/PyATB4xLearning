# functions with no return type and no parameters
def greet():
    print("Hello everyone")


# functions with no return type, but parameters
def Greet(name):  # name is parameter
    print("Hello", name.upper())


Greet("Monika Saini")  # name value should be defined here only


# functions with no return type, but default parameters
def say_hello_default_args(language="Python"):  # default argument
    print("Welcome to the", language.upper(), "Programming class")


say_hello_default_args()  # functions can be called without passing arguments,will take default one
say_hello_default_args("Java")  # functions can be called with passing arguments,will replace default one
say_hello_default_args(language="Ruby")  # positional argument


# positional argument = where parameter can be passed with or without giving keyword

# functions with parameters and return type
def sum_of_two_num(num1, num2):
    return num1 + num2


result = sum_of_two_num(10, 20)
print(result)


# functions with default parameters and return type
def product_of_two_nums(a=34, b=10):
    return a * b


product = product_of_two_nums(23, 45)
mul = product_of_two_nums(45)  # can be done ,we can omit any argument,as it is having default value
products = product_of_two_nums()
print(product)
print(products)
print(mul)
