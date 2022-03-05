import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Hip Hop", 3, 100.00)
        self.room_2 = Room("Soul", 4, 100.00)
        self.room_3 = Room("Rock", 4, 100.00)
        
        self.song_1 = Song("Stayin' Alive", "Bee Gees")
        self.song_2 = Song("The Boss", "Diana Ross")
        self.song_3 = Song("Everything Now", "Arcade Fire")
        self.song_4 = Song("Lose Yourself", "Eminem")
        self.song_5 = Song("This Time (I'm Gonna Try It My Way)", "DJ Shadow")

        self.guest_1 = Guest("Sandy", 50.00)
        self.guest_2 = Guest("Danny", 45.00)
        self.guest_3 = Guest("Holly", 75.00)
        self.guest_4 = Guest("Paul", 20.00)
        self.guest_5 = Guest("Maria", 60.00)

    # MVP tests:

    def test_room_has_name(self):
        self.assertEqual("Hip Hop", self.room_1.name)

    def test_can_update_room_name(self):
        self.room_2.name = "Heavy Metal"
        self.assertEqual("Heavy Metal", self.room_2.name)

    def test_room_has_playlist(self):
        self.assertEqual([], self.room_1.playlist)

    def test_room_has_guests(self):
        self.assertEqual([], self.room_1.guests)

    def test_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_1)
        expected = [self.song_1]
        self.assertEqual(expected, self.room_1.playlist)
        self.assertEqual(1, len(self.room_1.playlist))
    
    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        expected = [self.guest_1, self.guest_2]
        self.assertEqual(expected, self.room_1.guests)
        self.assertEqual(2, len(self.room_1.guests))

    def test_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_out_guest(self.guest_1)
        expected = [self.guest_2]
        self.assertEqual(expected, self.room_1.guests)
        self.assertEqual(1, len(self.room_1.guests))
    
    # Extension tests:

    def test_check_space_in_room(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.assertEqual(3, len(self.room_1.guests))

    def test_room_has_till(self):
        self.assertEqual(100, self.room_2.till)

    def test_can_increase_till(self):
        self.room_2.till += 15.00
        self.assertEqual(115, self.room_2.till)

    # def test_take_entry_fee(self):
    #     self.room_1.take_entry_fee(self.guest_1)
    #     self.assertEqual()