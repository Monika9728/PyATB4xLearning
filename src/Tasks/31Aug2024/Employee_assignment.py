# Class and Object Assignment
# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, print details,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.
class Employee:
    # attributes
    eid = None
    name = None
    age = None
    phone = None
    address = None

    # Creating Constructor
    def __init__(self, id, name, age, phone, address):
        print("I am a Default Constructor called immidiately after you create an object")
        self.eid = id
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    # behaviour
    def walk(self):
        print(self.name, "can walk")

    def talk(self):
        print(self.name, "can talk")

    def details(self):
        print("details")


employee1 = Employee(101, "Akash", "29", 9878989780, "Karnataka")
employee1.walk()
employee1.talk()
employee2 = Employee(102, "Madhav", "30", 8872980290, "Chennai")
employee2.walk()
employee2.talk()
