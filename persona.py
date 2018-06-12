#!/usr/bin/env python
'''character class'''


class Persona:
    def __init__(self, name='default_char', strength=1, speed=1, magic=0):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.magic = magic
        self.hp = 5 + ((self.strength + self.speed)) * (1 + self.magic)
        self.alive = True

    def is_alive(self):
        return self.alive

    def hp_mod(self):
        self.hp = 5 + ((self.strength + self.speed)) * (1 + self.magic)

    def str_mod(self, number):
        self.strength += number

    def spd_mod(self, number):
        self.speed += number

    def mag_mod(self, number):
        self.magic += number

    def check_hp(self):
        return self.hp

    def attack(self):
        return (1 + self.strength + self.speed + 2 * self.magic)

    def damage(self, number):
        self.hp -= number
        if (self.hp <= 0):
            self.alive = False
