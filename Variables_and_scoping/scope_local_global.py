# Run this code with the following terminal command
# python3 scope_local-global.py

# ------------------------------------------------------------


# Global variable (accessible throughout the entire program)
global_variable = "I am a global variable"

def my_function():
    # Local variable (only accessible within the function)
    local_variable = "I am a local variable"
    print(global_variable)  # This will work, as global_variable is accessible within the function
    print(local_variable)   # This will also work, as local_variable is accessible within the function

my_function()

print(global_variable)  # This will work, as global_variable is accessible outside the function
print(local_variable)   # This will raise an error, as local_variable is not accessible outside the function


