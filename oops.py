# initiate a class:
class Employee:
    # special method/ magic method/ dunder method: --> constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id = 123
        self.salry = 5000
        self.designation = "SDE"
        print("attributes/data executed successfully")

    def travel(self, destination):
        print("this travel method was called manually")
        print(f"Employee is now traveling to {destination}")

# Create an object/instance of the class:
sam = Employee()

# Access the attributes of the class:
# print(sam.designation)

# Access the methods of the class:
# sam.travel("Pahelgam")

print(type(sam))