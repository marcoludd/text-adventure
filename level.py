#!/usr/bin/env python
'''creating cool levels'''
import monster


class Level:
    def __init__(self, monster=True, treasure=True):
        if (monster):
            self.create_monster()
        self.treasure = treasure
        self.ambience = "\nYou are in a dark and cool cave entrance\n"

    def create_monster(self):
        self.monster_ = monster.Monster()

    def create_treasure(self):
        pass

    def level_description(self):
        description = self.ambience + 'You see a ' + self.monster_.name + '\n'
        print (description)