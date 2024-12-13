import unittest
from codeKata import Product, Checkout

class TestCheckoutSystem(unittest.TestCase):
    def setUp(self):
        self.checkout = Checkout()
        self.checkout.add_product(Product(name="A", unit_price=50, discount_quantity=3, discount_price=130))
        self.checkout.add_product(Product(name="B", unit_price=30, discount_quantity=2, discount_price=45))
        self.checkout.add_product(Product(name="C", unit_price=20))
        self.checkout.add_product(Product(name="D", unit_price=15))

    def test_single_item_no_discount(self):
        self.checkout.scan("C")
        total = self.checkout.calculate_total()
        self.assertEqual(total, 20)

    def test_multiple_items_no_discount(self):
        self.checkout.scan("C")
        self.checkout.scan("D")
        total = self.checkout.calculate_total()
        self.assertEqual(total, 35)

    def test_discount_applied(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        total = self.checkout.calculate_total()
        self.assertEqual(total, 130)

    def test_discount_with_remainder(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        total = self.checkout.calculate_total()
        self.assertEqual(total, 180)  

    def test_multiple_discounts(self):
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("A")
        self.checkout.scan("B")
        self.checkout.scan("B")
        total = self.checkout.calculate_total()
        self.assertEqual(total, 175) 
    def test_invalid_item(self):
        with self.assertRaises(ValueError):
            self.checkout.scan("Z")

    def test_empty_cart(self):
        total = self.checkout.calculate_total()
        self.assertEqual(total, 0)

if __name__ == "__main__":
    unittest.main()
