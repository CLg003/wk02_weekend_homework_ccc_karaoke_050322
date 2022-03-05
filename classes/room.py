class Room:
    def __init__(self, name):
        self.name = name
        self.playlist = []
        self.guests = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def check_in_guest(self, guest):
        self.guests.append(guest)
        