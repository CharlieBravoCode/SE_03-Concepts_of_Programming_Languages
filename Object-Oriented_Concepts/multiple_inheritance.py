class Parent1:
    def greet1(self):
        print("Hello from Parent1 class")

class Parent2:
    def greet2(self):
        print("Hello from Parent2 class")

class Child(Parent1, Parent2):
    pass

c = Child()
c.greet1()
c.greet2()


# Output:
# Hello from Parent1 class
# Hello from Parent2 class