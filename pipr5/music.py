class Artist:
    def __init__(self, first_name, last_name, nickname, albums=None, songs=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.albums = albums
        self.songs = songs


class Album:
    def __init__(self, title, publication_date, songs=None):
        self.title = title
        self.publication_date = publication_date
        self.songs = songs


class Song:
    def __init__(self, title, length):
        self.title = title
        self.length = length

    def play_song(self):
        print(f"The {self.title} is playing na na na for {self.length} seconds")
