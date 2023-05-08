class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

# Create an object (instance of the Dog class)
my_dog = Dog("Buddy", "Golden Retriever")

# Access object's attributes and methods
print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
my_dog.bark()        # Output: Buddy says: Woof!