import unittest

class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappucino': 3.20,
            'americano': 2.70
        }


class TestCoffeeMenu(unittest.TestCase):
    def get_price(self, item):
        return self.menu.get(item.lower())

    def add_item(self, item, price):
        self.menu[item.lower()] = price
    def setUp(self):
        self.menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price("espresso"), 3.00)



if __name__ == '__main__':
  unittest.main()
