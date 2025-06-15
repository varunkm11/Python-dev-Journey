# Prices
pizza_prices = {
    1: 100,   # Small
    2: 200,   # Medium
    3: 300    # Large
}

topping_prices = {
    1: ("Pepperoni", 50),
    2: ("Mushrooms", 40),
    3: ("Extra Cheese", 30)
}

# Start Order
name = input("Enter your name: ")
print(f"\nWelcome to Pizza Gallery, {name}!")

print("\nMenu:")
print("1. Small Pizza - ₹100")
print("2. Medium Pizza - ₹200")
print("3. Large Pizza - ₹300")

choice = int(input("\nEnter your choice (1, 2, or 3): "))

if choice in [1, 2, 3]:
    pizza_price = pizza_prices[choice]
    pizza_size = {1: "Small", 2: "Medium", 3: "Large"}[choice]
    print(f"{pizza_size} Pizza added to cart.")
else:
    print("Invalid choice. Please choose from the menu.")
    exit()

# Extra Toppings
topping_choice = 0
topping_cost = 0
topping_name = "None"

toppings = input("\nDo you want extra toppings? (yes/no): ").lower()
if toppings == "yes":
    print("\nTopping options:")
    print("1. Pepperoni - ₹50")
    print("2. Mushrooms - ₹40")
    print("3. Extra Cheese - ₹30")
    topping_choice = int(input("Choose topping (1, 2, or 3): "))

    if topping_choice in topping_prices:
        topping_name, topping_cost = topping_prices[topping_choice]
        print(f"{topping_name} added.")
    else:
        print("Invalid topping choice. No topping will be added.")
else:
    print("No extra toppings selected.")

# Quantity
quantity = int(input("\nHow many pizzas do you want?: "))
total_price = (pizza_price + topping_cost) * quantity

# Final Bill
print("\n--- Final Bill ---")
print(f"Customer Name: {name}")
print(f"Pizza Size: {pizza_size}")
print(f"Topping: {topping_name}")
print(f"Quantity: {quantity}")
print(f"Total Price: ₹{total_price}")
print("Thank you for ordering from Pizza Gallery!")
