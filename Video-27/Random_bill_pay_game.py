import random

# Input names separated by commas
Names = input("Enter the names separated by commas: ")

# Split and clean up the names
names = [name.strip() for name in Names.split(",")]

# Pick a random name
z = random.choice(names)

# Print the result
print(f"{z}, pay the bill!!")
