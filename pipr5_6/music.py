import time
import datetime


class Artist:
    def __init__(self, first_name, last_name, nickname, albums=None, songs=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.albums = albums
        self.songs = songs


class Album:
    def __init__(self, title, publication_date, songs):
        self.title = title
        self.publication_date = publication_date
        self.songs = songs

    def __len__(self):
        return self.total_time()

    def total_time(self):
        total_time = sum([s.time for s in self.songs], datetime.timedelta())
        hours, minutes, seconds = self.split_time_delta(total_time)
        return f"Total time of album is: {hours:02}:{minutes:02}:{seconds:02} (HH:mm:ss)"

    @staticmethod
    def split_time_delta(time_delta):
        """
        :param time_delta: Length of sum as a timedelta object
        :type time_delta: datetime.timedelta
        :rtype: tuple(int,int,int)
        """
        minutes, seconds = divmod(time_delta.seconds + time_delta.days * 86400, 60)
        hours, minutes = divmod(minutes, 60)
        return hours, minutes, seconds

    def play(self, first_song_index=0):
        for song_index in range(first_song_index, len(self.songs)):
            self.songs[song_index].play()


class Song:
    def __init__(self, title, time):
        """
        :param title: Title of the song.
        :type title: str
        :param length: Length of song as a time object
        :type length: datetime.timedelta
        """
        self.title = title
        self.time = time

    def play(self):
        print(f"The {self.title} is playing na na na for {self.time}")
        time.sleep(3)


s1 = Song("Przekorny los", datetime.timedelta(minutes=3, seconds=2))
s2 = Song("Nie daj sie", datetime.timedelta(minutes=2, seconds=10))
s3 = Song("Lalala", datetime.timedelta(minutes=1, seconds=10))

album = Album("Przeboje polskiej muzyki", datetime.datetime(day=2, month=11, year=2000), [s1, s2, s3])
album.play(1)
print(album.total_time())
