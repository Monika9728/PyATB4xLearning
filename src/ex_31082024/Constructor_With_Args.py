class Car:
    brand_name = None
    wheels = None
    breaks = None
    music = None
    air_bags = None
    ac = None

    # Default Constuctor:
    def __init__(self, name, wheel, breaka, music, airbags, ac):  # self means current state
        print("I am a Default Constructor called immidiately after you create an object")
        self.brand_name = name
        self.wheels = wheel
        self.breaks = breaka
        self.music = music
        self.air_bags = airbags
        self.ac = ac

    def speed(self):
        print("Maximum speed is:120km/h")
        print("Speed of", self.brand_name, "is: 150 kmph")
        return None

    def songs(self):
        print("You can play music too")


cars = Car("Mercedes Benz", "4 wheels", True, True, True, "Full")
print(cars.brand_name)
print(cars.wheels)
print(cars.ac)
print(cars.music)
print(cars.air_bags)
cars.speed()

cars2 = Car("Rubicon", "4 wheels", True, True, True, "Full")
print(cars2.brand_name)
print(cars2.music)
print(cars2.wheels)
print(cars2.air_bags)
print(cars2.ac)
