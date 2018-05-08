#!/usr/bin/env python
'''creating cool levels'''
import monster
import persona
import item
from random import randrange

monster_dict = {1: 'goblin',
                2: 'skeleton',
                3: 'dragon',
                4: 'golem',
                5: 'gargoyle'
               }

class Level:
    def __init__(self, ambience='nothing', monster=True, item=True):
        if (monster):
            self.create_monster()
        self.ambience = ambience
        self.monster = monster
        self.item = item

    def create_monster(self):
        name = monster_dict[randrange(1,5)]
        strength = randrange(-1,3)
        speed = randrange(-1,3)
        magic = randrange(0, 2)
        self.monster = persona.Persona(name, strength, speed, magic)


