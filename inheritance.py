class parent:
    def __init__(self, name):
        self.name = name 

    def greet(self):
        print(f"Hello, {self.name}!")

class child1(parent):
    def play(self):
        print(f"{self.name} is playing!")

class child2(child1):
    def study(self):
        print(f"{self.name} is studying!")

child1 = child1("John")
child2 = child2("Jane")

child1.greet()
child1.play()

child2.greet()  
child2.study()
child2.play()