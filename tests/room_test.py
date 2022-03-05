import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest
from classes.bar_drink import BarDrink

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

        self.guest_1 = Guest("Sandy", 50.00, "Everything Now")
        self.guest_2 = Guest("Danny", 45.00, "Greased Lightning")
        self.guest_3 = Guest("Holly", 75.00, "Moon River")
        self.guest_4 = Guest("Paul", 20.00, "Lose Yourself")
        self.guest_5 = Guest("Maria", 60.00, "Stayin' Alive")

        self.drink_1 = BarDrink("lager", 3.50)
        self.drink_2 = BarDrink("prosecco", 19.00)
        self.drink_3 = BarDrink("cocktail", 6.00)
        self.drink_4 = BarDrink("coca cola", 2.00)
        self.drink_5 = BarDrink("water", 0.00)

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

    def test_can_take_entry_fee(self):
        self.room_1.take_entry_fee(self.guest_1)
        self.assertEqual(40, self.guest_1.cash)
        self.assertEqual(110, self.room_1.till)

    # Advanced extension tests:

    def test_can_find_song_by_title(self):
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_1)
        self.room_1.add_song_to_playlist(self.song_3)
        result = self.room_1.find_song_by_title("Everything Now")
        self.assertEqual(self.song_3, result)

    def test_new_guest_tab_added(self):
        self.room_1.start_new_guest_tab(self.guest_1)
        expected = {self.guest_1 : 0}
        self.assertEqual(expected, self.room_1.guest_tabs)

    def test_guest_tab_increased_entry_fee(self):
        self.room_1.add_entry_fee_to_tab(self.guest_1)
        expected = {self.guest_1 : 10}
        self.assertEqual(expected, self.room_1.guest_tabs)

    def test_guest_tab_increased_bar_drinks(self):
        self.room_1.add_entry_fee_to_tab(self.guest_1)
        self.room_1.add_bar_drink_to_tab(self.guest_1, self.drink_2)
        self.room_1.add_bar_drink_to_tab(self.guest_1, self.drink_3)
        self.room_1.add_bar_drink_to_tab(self.guest_1, self.drink_4)
        expected = {self.guest_1 : 37}
        self.assertEqual(expected, self.room_1.guest_tabs)

    def test_guest_tab_paid(self):
        self.room_1.add_entry_fee_to_tab(self.guest_1)
        self.room_1.add_bar_drink_to_tab(self.guest_1, self.drink_2)
        self.room_1.add_bar_drink_to_tab(self.guest_1, self.drink_3)
        self.room_1.add_bar_drink_to_tab(self.guest_1, self.drink_4)
        self.room_1.clear_fully_paid_guest_tab(self.guest_1)
        expected = {}
        self.assertEqual(expected, self.room_1.guest_tabs)
        self.assertEqual(13, self.guest_1.cash)
        self.assertEqual(137, self.room_1.till)

