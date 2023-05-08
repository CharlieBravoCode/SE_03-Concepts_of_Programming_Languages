# Run this code with the following terminal command
# python3 scope_static.py

# ------------------------------------------------------------



x = 10  # Global variable

def outer():
    y = 20  # Enclosing variable (local to outer())

    def inner():
        z = 30  # Local variable
        print(x, y, z)  # Access all variables in the lexical scope

    inner()

outer()
# Output: 10 20 30

