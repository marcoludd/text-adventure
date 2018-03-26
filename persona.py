#!/usr/bin/env python
'''character class'''


class Persona:
    def __init__(self, name='default_char', strenght=1, speed=1, magic=0):
        self.name = name
        self.strenght = strenght
        self.speed = speed
        self.magic = magic

    def get_name(self):
        return self.name

    def set_strenght(self, strenght):
        self.strenght = strenght

    def get_strenght(self):
        return self.strenght

    def set_speed(self, speed):
        self.strenght = speed

    def set_magic(self, magic):
        self.magic = magic


