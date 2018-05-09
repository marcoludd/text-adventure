#!/usr/bin/env python
'''creating cool levels'''
import persona

from random import randrange


class Level:
    def __init__(self, ambience='nothing', monster_name='goblin'):
        self.ambience = ambience
        self.create_monster(monster_name)

    def create_monster(self, monster_name):
        name = monster_name
        strength = randrange(0, 3)
        speed = randrange(0, 2)
        magic = randrange(0, 2)
        self.monster = persona.Persona(name, strength, speed, magic)

