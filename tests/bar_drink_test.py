import unittest
from classes.bar_drink import BarDrink

class TestBarDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = BarDrink("lager", 3.50)
        self.drink_2 = BarDrink("prosecco", 19.00)
        self.drink_3 = BarDrink("cocktail", 6.00)
        self.drink_4 = BarDrink("coca cola", 2.00)
        self.drink_5 = BarDrink("water", 0.00)
    
    def test_drink_has_name(self):
        self.assertEqual("lager", self.drink_1.name)

    def test_can_update_drink_name(self):
        self.drink_1.name = "beer"
        self.assertEqual("beer", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink_1.price)

    def test_can_update_drink_price(self):
        self.drink_1.price = 4.50
        self.assertEqual(4.50, self.drink_1.price)