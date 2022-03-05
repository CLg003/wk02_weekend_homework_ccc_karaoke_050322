class Room:
    def __init__(self, name):
        self.name = name
        self.playlist = []
        self.guests = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    