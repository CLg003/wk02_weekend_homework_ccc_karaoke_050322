import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Stayin' Alive", "Bee Gees")

    def test_song_has_title(self):
        self.assertEqual("Stayin' Alive", self.song_1.title)

    def test_can_update_song_title(self):
        self.song_1.title = "Night Fever"
        self.assertEqual("Night Fever", self.song_1.title)