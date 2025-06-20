def greet(name):
    """Function to greet a person by name."""
    print(f"Hello, {name}!")

def add(a, b):
    """Function to add two numbers and return the result."""
    return a + b

def is_even(number):
    """Function to check if a number is even."""
    return number % 2 == 0

# Example usage:
greet("Alice")
result = add(5, 7)
print(f"5 + 7 = {result}")

num = 10
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")