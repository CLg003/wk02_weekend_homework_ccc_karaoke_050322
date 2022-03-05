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
            self.add_entry_fee_to_tab(guest) # Advanced extensions

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.clear_fully_paid_guest_tab(guest) # Advanced extensions
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

    def add_entry_fee_to_tab(self, guest):
        entry_fee = 10.00
        self.start_new_guest_tab(guest)
        self.guest_tabs[guest] += entry_fee
    
    def add_bar_drink_to_tab(self, guest, drink):
        self.start_new_guest_tab(guest)
        self.guest_tabs[guest] += drink.price

    def clear_fully_paid_guest_tab(self, guest):
        total_bill_to_pay = self.guest_tabs[guest]
        if guest.cash >= total_bill_to_pay:
            guest.cash -= total_bill_to_pay
            self.till += total_bill_to_pay
            self.guest_tabs.pop(guest)

    def add_song_playlist_to_room(self, playlist):
        self.playlist += playlist
