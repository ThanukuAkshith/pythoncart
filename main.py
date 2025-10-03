

from cart import view_products, add_to_cart, view_cart, update_cart, remove_from_cart, checkout

def menu():
    while True:
        print("\n===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            else:
                add_to_cart(product_id, quantity)
        elif choice == "3":
            view_cart()
        elif choice == "4":
            product_id = int(input("Enter Product ID to update: "))
            quantity = int(input("Enter new Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            else:
                update_cart(product_id, quantity)
        elif choice == "5":
            product_id = int(input("Enter Product ID to remove: "))
            remove_from_cart(product_id)
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Exiting Shopping Cart. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
