class Room:
    def __init__(self, name, max_guests):
        self.name = name
        self.max_guests = max_guests
        self.playlist = []
        self.guests = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def check_in_guest(self, guest):
        if len(self.guests) < self.max_guests:
            self.guests.append(guest)

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)