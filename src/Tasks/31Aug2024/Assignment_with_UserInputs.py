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
    def __init__(self):
        print("I am a Default Constructor called immidiately after you create an object")
        self.eid = input("Enter Employee Id: ")
        self.name = input("Enter Employee Name: ")
        self.age = input("Enter Employee Age: ")
        self.phone = input("Enter Employee Phone Number: ")
        self.address = input("Enter Employee Address: ")

    # behaviour
    def walk(self):
        print(self.name, "can walk")

    def talk(self):
        print(self.name, "can talk")

    def print_employee(self):
        print("The Employee Details are given below:\n")
        print("Employee ID is:", self.eid, "Employee Name is:", self.name, "Employee Age is:", self.age,
              "Employee Phone number is:", self.phone, "Employee Address is:", self.address,sep="\n")


employee1 = Employee()
employee1.walk()
employee1.talk()
employee1.print_employee()
employee2 = Employee()
employee2.walk()
employee2.talk()
employee2.print_employee()
