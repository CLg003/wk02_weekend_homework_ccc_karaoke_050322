import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Sandy")

    def test_guest_has_name(self):
        self.assertEqual("Sandy", self.guest_1.name)

    def test_can_update_guest_name(self):
        self.guest_1.name = "Sandra"
        self.assertEqual("Sandra", self.guest_1.name)