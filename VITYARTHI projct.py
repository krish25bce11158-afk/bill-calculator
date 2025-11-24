

# 1. DATA STRUCTURE: List of Tuples
# We use tuples () because the item name and price should not change.
menu = [
    ("Burger", 10.50),
    ("Fries", 3.00),
    ("Soda", 2.50),
    ("Ice Cream", 5.00),
    ("Salad", 7.25)
]


def show_menu():
    """Print the menu with item numbers and prices."""
    print("--- Welcome to the Tuple Diner ---")
    print("Here is our menu:")
    for index, item in enumerate(menu, start=1):
        name, price = item
        print(f"{index}. {name} -- ${price:.2f}")
    print("\nType the number of the item to order. Type '0' to finish.")


def take_order():
    """Handle user input and build the order list."""
    order = []

    while True:
        try:
            choice = int(input("Enter item number: "))

            if choice == 0:
                break

            if 1 <= choice <= len(menu):
                selected_item = menu[choice - 1]
                order.append(selected_item)
                print(f"Added {selected_item[0]} to your order.")
            else:
                print("Invalid number, try again.")
        except ValueError:
            print("Please enter a valid number only.")

    return order


def print_receipt(order):
    """Print a simple receipt and total amount."""
    total_cost = 0.0
    print("\n--- YOUR RECEIPT ---")

    for name, price in order:
        print(f"{name}: ${price:.2f}")
        total_cost += price

    print("-" * 20)
    print(f"TOTAL DUE: ${total_cost:.2f}")
    print("--------------------")


def main():
    show_menu()
    order = take_order()
    print_receipt(order)


if __name__ == "__main__":
    main()

