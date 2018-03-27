#!/usr/bin/env python
'''Controlling it all'''
import monster

class Level:
    def __init__(self, monster=True, treasure=True):
    self.monster = monster
    self.treasure = treasure

    def create_monster(self):
        monster_ = monster.Monster()

    def create_treasure(self):
        pass

    def create_description(self):
        pass