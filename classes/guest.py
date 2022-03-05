class Guest:
    def __init__(self, name, cash, favourite_song):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song

    # Advanced extensions methods:

    def cheer_for_favourite_song(self, room, song_title):
        if room.find_song_by_title(song_title):
            return "Whoo, they have my favourite song!"
        return "Aw, I can't sing my favourite song."
        