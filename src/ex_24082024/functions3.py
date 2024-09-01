# def and call is necessary for user defined functions
def greet_to_all_of_you():
    print("Hello everyone")


def greet():
    print("Greeting everyone")
    greet_to_all_of_you()  # calling function inside another function


greet()
