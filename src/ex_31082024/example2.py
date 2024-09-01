class Dog: #class name always starts with capital letter
    name = None #always set to none
    breed = None
    color = None

    def bark(self):
        print("Dog 1 can bark")

    def see(self):
        print("Dog 1 can see")

    def eat(self):
        print("Dog 1 can eat")

    def run(self):
        print("Dog 1 can run")


dog1 = Dog()
dog1.name = "Brownie"
dog1.breed = "German"
dog1.color = "Brown"
print(dog1.name)
print(dog1.color)
print(dog1.breed)
dog1.bark()
dog1.see()
dog1.eat()
dog1.run()

dog2 = Dog()
dog1.name = "Coffee"
dog1.breed = "Lebra"
dog1.color = "White"
print(dog1.name)
print(dog1.color)
print(dog1.breed)
