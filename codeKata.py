class Product:
    def __init__(self, name, unit_price, discount_quantity=None, discount_price=None):
        self.name = name
        self.unit_price = unit_price
        self.discount_quantity = discount_quantity
        self.discount_price = discount_price


class Checkout:
    def __init__(self):
        self.products = {}  # initilize Dict to store available products.
        self.cart = {}      # initilize Dict to store items scanned.

    def add_product(self, product):
        self.products[product.name] = product

    def scan(self, item):
        if item not in self.products:
            raise ValueError(f"Product '{item}' is not available.")
        self.cart[item] = self.cart.get(item, 0) + 1

    def calculate_total(self):
        total = 0

        for item, quantity in self.cart.items():
            product = self.products[item]

            if product.discount_quantity and quantity >= product.discount_quantity:
                discount_sets = quantity // product.discount_quantity
                remaining_items = quantity % product.discount_quantity

                total += discount_sets * product.discount_price
                total += remaining_items * product.unit_price
            else:
                total += quantity * product.unit_price
        return total


# Example for checkout supermarket system
if __name__ == "__main__":
    # Initialize checkout 
    checkout = Checkout()
    checkout.add_product(Product(name="A", unit_price=50, discount_quantity=3, discount_price=130))
    checkout.add_product(Product(name="B", unit_price=30, discount_quantity=2, discount_price=45))
    checkout.add_product(Product(name="C", unit_price=20))
    checkout.add_product(Product(name="D", unit_price=15))
    items_to_scan = ["A", "A", "A", "B", "B", "D"]
    for item in items_to_scan:
        checkout.scan(item)
    total_price = checkout.calculate_total()
    print(f"Total Price: {total_price}")
