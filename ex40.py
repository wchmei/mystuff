# -*- coding: utf-8 -*-
class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["happy birthday to you",
                       "I don't want get sued",
                       "So I'll stop rigth there"])
bulls_on_parade = Song(["There rally around the family",
                        "With pockets full of sheells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()