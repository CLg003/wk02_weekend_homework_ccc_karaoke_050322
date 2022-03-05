# from song import Song
# from room import Room

class Guest:
    def __init__(self, name, cash, favourite_song):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song
        
    def cheer_for_favourite_song(self, room, song_title):
        if room.find_song_by_title(song_title):
            return "Whoo, they have my favourite song!"
        return "Aw, I can't sing my favourite song."

# guest_1 = Guest("Sandy", 50.00, "Everything Now")

# room_1 = Room("Hip Hop", 3, 100.00)

# song_1 = Song("Stayin' Alive", "Bee Gees")
# song_2 = Song("The Boss", "Diana Ross")
# song_3 = Song("Everything Now", "Arcade Fire")

# room_1.add_song_to_playlist(song_1)
# room_1.add_song_to_playlist(song_1)
# room_1.add_song_to_playlist(song_3)

# print(guest_1.cheer_for_favourite_song(room_1, guest_1.favourite_song))