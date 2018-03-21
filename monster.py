#!/usr/bin/env python
'''monster class'''
import character

class Monster(Character):
    def __init__ (self, name, strenght, speed, growl):
        Character.__init__(self, name, strenght, speed, 0)
        self.growl = growl

    def growl(self):
        return self.growl