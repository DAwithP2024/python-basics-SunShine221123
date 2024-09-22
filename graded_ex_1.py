import re

# Provided products dictionary
products = {
    "IT products": {
        "Laptop": 1000,
        "Mouse": 50,
        "Keyboard": 80
    },
    "Electronics": {
        "Smartphone": 800,
        "Headphones": 150,
        "Smartwatch": 200
    }
}

# Function to validate name
def validate_name(name):
    if re.match("^[A-Za-z]+ [A-Za-z]+$", name):
        return True
    return False

# Function to validate email
def validate_email(email):
    if "@" in email:
        return True
    return False

# Function to display categories
def display_categories():
    for i, category in enumerate(products.keys(), 1):
        print(f"{i}. {category}")

# Function to display products
def display_products(products_list):
    for i, (product, price) in enumerate(products_list.items(), 1):
        print(f"{i}. {product} - ${price}")

# Function to display sorted products
def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list.items(), key=lambda x: x[1], reverse=(sort_order == 2))
    for i, (product, price) in enumerate(sorted_products, 1):
        print(f"{i}. {product} - ${price}")
    return sorted_products

# Function to add product to cart
def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

# Function to generate receipt
def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Products purchased:")
    for product, quantity in cart:
        print(f"{product} - Quantity: {quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# Main function
def main():
    # Ask user for name and email address
    while True:
        name = input("Enter your name (first and last name): ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please enter a valid first and last name.")

    while True:
        email = input("Enter your email address: ")
        if validate_email(email):
            break
        else:
            print("Invalid email. Please enter a valid email address.")

    # Display categories and handle user interaction
    cart = []
    while True:
        display_categories()
        category_choice = int(input("Enter the number of the category you want to explore: "))
        
        if category_choice < 1 or category_choice > len(products):
            print("Invalid choice. Please enter a valid number.")
            continue
        
        selected_category = list(products.keys())[category_choice - 1]
        selected_products = products[selected_category]
        
        while True:
            display_products(selected_products)
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")
            
            option = int(input("Enter your choice: "))
            
            if option == 1:
                product_choice = int(input("Enter the number of the product you want to buy: "))
                if product_choice < 1 or product_choice > len(selected_products):
                    print("Invalid choice. Please enter a valid number.")
                    continue
                
                selected_product = list(selected_products.keys())[product_choice - 1]
                quantity = int(input(f"Enter the quantity of {selected_product} you want to buy: "))
                add_to_cart(cart, selected_product, quantity)
            
            elif option == 2:
                sort_order = int(input("Enter 1 for ascending order or 2 for descending order: "))
                display_sorted_products(selected_products, sort_order)
            
            elif option == 3:
                break
            
            elif option == 4:
                if cart:
                    total_cost = sum(selected_products[product] * quantity for product, quantity in cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

if __name__ == "__main__":
    main()
