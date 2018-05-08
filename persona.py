#!/usr/bin/env python
'''character class'''


class Persona:
    def __init__(self, name='default_char', strength=1, speed=1, magic=0):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.magic = magic
        self.hp = (2*(self.strength+self.speed))*(1 + self.magic)
    
    def hp_mod(self):
        self.hp = (2*(self.strength+self.speed))*(1 + self.magic)

    def str_mod(self, number):
        self.hp += number

