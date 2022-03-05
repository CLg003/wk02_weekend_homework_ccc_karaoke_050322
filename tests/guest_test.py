import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Sandy", 50.00, "Everything Now")

    # MVP tests:

    def test_guest_has_name(self):
        self.assertEqual("Sandy", self.guest_1.name)

    def test_can_update_guest_name(self):
        self.guest_1.name = "Sandra"
        self.assertEqual("Sandra", self.guest_1.name)
    
    # Extensions tests:

    def test_guest_has_cash(self):
        self.assertEqual(50, self.guest_1.cash)
        
    def test_can_reduce_guest_cash(self):
        self.guest_1.cash -= 15.00
        self.assertEqual(35, self.guest_1.cash)

    # Advanced extension tests:

    def test_guest_has_favourite_song(self):
        self.assertEqual("Everything Now", self.guest_1.favourite_song)
    
    def test_can_update_guest_favourite_song(self):
        self.guest_1.favourite_song = "Trips"
        self.assertEqual("Trips", self.guest_1.favourite_song)