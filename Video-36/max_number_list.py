num = int(input("How many numbers will you enter? "))
numbers = []  # List to store all entered numbers
#max_number = numbers[0]

for i in range(1, num + 1):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)

max_number = numbers[0]
for i in numbers:
    if i > max_number:
        max_number = i

print(f"The list of numbers is: {numbers}")
print(f"The maximum number in th list is : {max_number}")