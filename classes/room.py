class Room:
    def __init__(self, name, max_guests, till):
        self.name = name
        self.max_guests = max_guests # Extensions property
        self.till = till
        self.playlist = []
        self.guests = []
        self.guest_tabs = {} # Advanced extensions property

# MVP methods:

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def check_in_guest(self, guest):
        if len(self.guests) < self.max_guests: # Extensions condition
            self.guests.append(guest)

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

# Extensions method:

    def take_entry_fee(self, guest):
        entry_fee = 10.00
        if guest.cash >= entry_fee:
            guest.cash -= entry_fee
            self.till += entry_fee

# Advanced extensions methods:

    def find_song_by_title(self, song_title):
        for song in self.playlist:
            if song_title == song.title:
                return song

    def start_new_guest_tab(self, guest):
        if guest not in self.guest_tabs:
            self.guest_tabs[guest] = 0