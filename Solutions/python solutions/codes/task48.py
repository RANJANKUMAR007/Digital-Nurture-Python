import math

class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

cart = ShoppingCart()
cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 1000, 2))
cart.add_item(CartItem("Keyboard", 2000, 1))
cart.remove_item("Mouse")

subtotal = cart.calculate_total()
gst = subtotal * 0.18
total = subtotal + gst

print("--- Receipt ---")
for item in cart.items:
    print(f"{item.name} x {item.quantity}: Rs. {item.price * item.quantity}")
print(f"Subtotal: Rs. {subtotal}")
print(f"GST (18%): Rs. {gst:.2f}")
print(f"Total: Rs. {math.ceil(total)}")
