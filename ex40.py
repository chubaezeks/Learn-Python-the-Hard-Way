
#A first class example
#We create a class this way.
class Song(object):

#a class can't work without the initialiser
    def __init__(self, lyrics):
        self.lyrics = lyrics
#we define another function has a for loop with the previous function and prints out the result
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

#These are the scripts wrapped up within these objects.
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song (["They rally around the family",
                            "With pockets full of shells"])


free = Song(["Now I'm feeling freeier than I've ever been. ",
            "Now you're feeling freeier than you've ever been.",
            "Really you feel trapped, no need to pretend."])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

free.sing_me_a_song()
