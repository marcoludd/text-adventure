#!/usr/bin/env python
'''player class'''
import character

class Player(Character):
    def __init__ (self, name, strenght, speed, magic, job):
        self.name = name
        self.job = job