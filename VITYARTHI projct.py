# 1. DATA STRUCTURE: List of Tuples
# We use tuples () because the item name and price should not change.
menu = [
    ("Burger", 10.50),  # Tuple 0
    ("Fries", 3.00),  # Tuple 1
    ("Soda", 2.50),  # Tuple 2
    ("Ice Cream", 5.00),  # Tuple 3
    ("Salad", 7.25)  # Tuple 4
]

order = []  # A list to store what the user buys
total_cost = 0.0

print("--- Welcome to the Tuple Diner ---")

# 2. DISPLAY THE MENU
# enumerate() is a handy trick that gives us the index (i) and the item tuple
print("Here is our menu:")
for i, item in enumerate(menu):
    # item[0] is the Name, item[1] is the Price
    print(f"{i + 1}. {item[0]} -- ${item[1]:.2f}")

print("\nType the number of the item to order. Type '0' to finish.")

# 3. THE LOGIC LOOP
while True:
    try:
        choice = int(input("Enter item number: "))

        if choice == 0:
            break

        # Check if the number is valid (between 1 and the length of the menu)
        if 1 <= choice <= len(menu):
            # We adjust for 0-based index (User types 1, we need index 0)
            selected_item = menu[choice - 1]

            # Add to our order list
            order.append(selected_item)
            print(f"Added {selected_item[0]} to your order.")
        else:
            print("Invalid number, try again.")

    except ValueError:
        print("Please enter a number only.")

# 4. CALCULATE RECEIPT
print("\n--- YOUR RECEIPT ---")
for item in order:
    # We unpack the tuple easily here
    name, price = item
    print(f"{name}: ${price:.2f}")
    total_cost += price

print("-" * 20)
print(f"TOTAL DUE: ${total_cost:.2f}")
print("--------------------")