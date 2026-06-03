class Product:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Perishable(Product):
    def __init__(self, item_id, name, price, expiry_date):
        super().__init__(item_id, name, price)
        self.expiry_date = expiry_date

class Electronics(Product):
    def __init__(self, item_id, name, price, warranty_period):
        super().__init__(item_id, name, price)
        self.warranty_period = warranty_period

inventory = {}
stock_levels = {}

def add_product(product, qty):
    inventory[product.item_id] = product
    stock_levels[product.item_id] = stock_levels.get(product.item_id, 0) + qty

apple = Perishable("P001", "Apple", 2.0, "2026-06-10")
phone = Electronics("E001", "Smartphone", 500.0, "2 Years")
banana = Perishable("P002", "Banana", 1.0, "2026-06-05")

add_product(apple, 10)
add_product(phone, 3)
add_product(banana, 40)

low_stock_threshold = 5
low_stock_alerts = {item_id for item_id, qty in stock_levels.items() if qty < low_stock_threshold}

print("Inventory Summary:")
for item_id, product in inventory.items():
    qty = stock_levels[item_id]
    p_type = product.__class__.__name__
    print(f"{product.name} ({p_type}) - Price: ${product.price}, Stock: {qty}")

print("\nLow Stock Alerts (IDs):")
print(low_stock_alerts)
