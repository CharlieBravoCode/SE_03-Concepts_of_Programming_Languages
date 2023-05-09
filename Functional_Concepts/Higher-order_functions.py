def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]

# Using Python's built-in map() function with the double function as an argument
doubled_numbers = map(double, numbers)

# Convert the result to a list and print it
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]


