import re

products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))
    return sorted_products

def display_products(products):
    for category, items in products.items():
        print(f"\n{category}:")
        sorted_products = display_sorted_products(items, "asc")
        for product, price in sorted_products:
            print(f"{product}: ${price:.2f}")

def display_categories():
    print("Available Categories:")
    for index, category in enumerate(products.keys()):
        print(f"{index}: {category}")

def add_to_cart(cart, product, quantity):
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    print("\nYour Cart:")
    total_cost = 0
    for product, quantity in cart.items():
        price = next((p[1] for c in products.values() for p in c if p[0] == product), 0)
        cost = price * quantity
        total_cost += cost
        print(f"{product}: {quantity} x ${price:.2f} = ${cost:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("Items Purchased:")
    for product, quantity in cart.items():
        print(f"{product}: {quantity}")
    print(f"Total Cost: ${total_cost:.2f}")

def validate_name(name):
    return len(name.strip()) > 0  # Validate that the name is not empty

def validate_email(email):
    # Use regex to validate the email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def main():
    cart = {}
    display_categories()
    display_products(products)
    
    while True:
        product = input("\nEnter product name to add to cart (or 'done' to finish): ")
        if product.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        add_to_cart(cart, product, quantity)
    
    display_cart(cart)
    
    name = input("Enter your name: ")
    while not validate_name(name):
        name = input("Invalid name. Enter your name again: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        email = input("Invalid email. Enter your email again: ")

    address = input("Enter your address: ")
    
    total_cost = sum(next((p[1] for c in products.values() for p in c if p[0] == product), 0) * quantity for product, quantity in cart.items())
    
    generate_receipt(name, email, cart, total_cost, address)

if __name__ == "__main__":
    main()
