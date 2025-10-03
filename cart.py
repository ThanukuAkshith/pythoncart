# cart.py

from products import products

# Global cart list
cart = []
max_items = 8

def view_products():
    print("\n===== Available Products =====")
    for p in products:
        print(f"ID: {p['id']} | {p['name']} | Price: ₹{p['price']}")
    print("="*30)


def add_to_cart(product_id, quantity):
    global cart
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        print("Invalid Product ID.")
        return


    if len(cart) >= max_items and not any(item["id"] == product_id for item in cart):
        print("Cart limit reached (max 8 items).")
        return


    for item in cart:
        if item["id"] == product_id:
            item["quantity"] += quantity
            print(f"✅ Updated {product['name']} quantity to {item['quantity']}.")
            return

 
    cart.append({
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })
    print(f"Added {product['name']} x{quantity} to cart.")


def view_cart():
    global cart
    if not cart:
        print("\n🛒 Cart is empty.")
        return
    print("\n===== Your Cart =====")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} | ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
    print(f"Total Amount: ₹{total}")
    print("="*30)


def update_cart(product_id, quantity):
    global cart
    for item in cart:
        if item["id"] == product_id:
            item["quantity"] = quantity
            print(f"Updated {item['name']} to {quantity}.")
            return
    print("Product not found in cart.")


def remove_from_cart(product_id):
    global cart
    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            print(f"Removed {item['name']} from cart.")
            return
    print("Product not found in cart.")


def checkout():
    global cart
    if not cart:
        print("Cart is empty, nothing to checkout.")
        return
    view_cart()
    print("Thank you for shopping with us!")
    cart.clear()
