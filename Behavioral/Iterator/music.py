

########################### WITH CLASS ###########################
class Playlist:
    def __init__(self, songs):
        self.songs = songs
        self.value = 0
        self.end = len(self.songs) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return self.songs[current]


tunes = ["Collide", "One Day", "Beautiful", "Stan", "The Kill"]
song = Playlist(tunes)
print(next(song))
print(next(song))
print(next(song))
print()

########################### WITH GENERATOR ###########################
def my_range(songs):
    current = 0
    while True:
        yield songs[current]
        current += 1


nums = my_range(tunes)
print(next(nums))
print(next(nums))
print(next(nums))