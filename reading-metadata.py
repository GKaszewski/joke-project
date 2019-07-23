from eyed3 import id3

song = id3.Tag()
song.parse('test.mp3')
print(song.artist)
print(song.album)
print(song.title)