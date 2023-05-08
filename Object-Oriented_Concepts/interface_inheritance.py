from abc import ABC, abstractmethod

class GreetInterface(ABC):
    @abstractmethod
    def greet(self):
        pass

class GreetImplementation(GreetInterface):
    def greet(self):
        print("Hello from GreetImplementation class")

g = GreetImplementation()
g.greet()

# Output:
# Hello from GreetImplementation class