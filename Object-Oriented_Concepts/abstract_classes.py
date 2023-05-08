from abc import ABC, abstractmethod

class AbstractGreet(ABC):
    @abstractmethod
    def greet(self):
        pass

    def hello(self):
        print("Hello from non-abstract method")

class GreetImplementation(AbstractGreet):
    def greet(self):
        print("Hello from GreetImplementation class")

g = GreetImplementation()
g.greet()
g.hello()

# Output:
# Hello from GreetImplementation class
# Hello from non-abstract method
