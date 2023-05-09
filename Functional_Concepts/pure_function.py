# A pure function with referential transparency
def add(x, y):
    return x + y

result1 = add(2, 3)  # Output: 5
result2 = add(2, 3)  # Output: 5 (same output for the same input)

print(result1 == result2)  # Output: True

