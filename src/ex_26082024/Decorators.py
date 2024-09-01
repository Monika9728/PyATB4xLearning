# Decorators in Python
# Decorators in Python are a way to modify a function or class without changing its source code

def my_Decorators(func):
    #     two parts
    # wrapper and call
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after  the function is called")

    return wrapper()

@my_Decorators
def drive_Bike():
    print("I am driving")
