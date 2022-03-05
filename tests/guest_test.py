import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Sandy", 50.00, "Everything Now")

        self.room_1 = Room("Hip Hop", 3, 100.00)

        self.song_1 = Song("Stayin' Alive", "Bee Gees")
        self.song_2 = Song("The Boss", "Diana Ross")
        self.song_3 = Song("Everything Now", "Arcade Fire")

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

    def test_can_cheer_for_favourite_song(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_3)
        result = self.guest_1.cheer_for_favourite_song(self.room_1, self.guest_1.favourite_song)
        self.assertEqual("Whoo, they have my favourite song!", result)
        