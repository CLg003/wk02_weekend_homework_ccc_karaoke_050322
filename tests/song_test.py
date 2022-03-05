import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Stayin' Alive", "Bee Gees")

    # MVP tests:
    
    def test_song_has_title(self):
        self.assertEqual("Stayin' Alive", self.song_1.title)

    def test_can_update_song_title(self):
        self.song_1.title = "Night Fever"
        self.assertEqual("Night Fever", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Bee Gees", self.song_1.artist)

    # @unittest.skip("delete this line to run the test")
    def test_can_update_song_artist(self):
        self.song_1.artist = "John Travolta"
        self.assertEqual("John Travolta", self.song_1.artist)