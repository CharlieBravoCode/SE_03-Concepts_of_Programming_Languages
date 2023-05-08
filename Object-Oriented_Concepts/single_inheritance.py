# Single inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

# Create an object (instance of the Dog class)
my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says: Woof!
