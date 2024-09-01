# constructor
# PURPOSE : --> to assign values no return type
# Special Function in class ,__init__()
# It will be automatically called,However one thing to be noted that unlike JAVA or C++,
# constructors are not named same as class in Python, for eg:
class Car:
    brand_name = None
    wheels = None
    breaks = None
    music = None
    air_bags = None
    ac = None

    # Default Constuctor:
    def __init__(self):
        print("I am a Default Constructor called immidiately after you create an object")

    def speed(self):
        print("Maximum speed is:120km/h")


    def songs(self):
        print("You can play music too")


cars = Car()
cars.brand_name = "Verna"
