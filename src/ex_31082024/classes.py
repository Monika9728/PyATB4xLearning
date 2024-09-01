# Class
# objects
# classes have attributes and behaviour which means data members and member functions.for example
#     human

class Person:
    # attributes
    id = None
    name = None
    age = None
    gender = None
    email = None
    phone_number = None
    address = None


# behaviour
def talk(self):  # self - this ,self will be the first argument in every behaviour
    print("I can talk")


def sleep(self, name):  # args with return
    print("I can sleep")
    return None


def walk(self):
    print("I can walk too")


def walk_return(self):  # no args with return type
    return "I can walk and return"


# Creates an Object of the Class
# ObjectRef = ClassName() -> Object

vaanika = Person()
vaanika.id = 101
vaanika.name = "Vaanika"
print(vaanika.id)
print(vaanika.name)
print(vaanika.age)
print(vaanika.email)
print(vaanika.address)
print(vaanika.phone_number)
vaanika.talk()
