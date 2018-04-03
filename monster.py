#!/usr/bin/env python
'''monster class'''
import persona
from random import randrange


class Monster(persona.Persona):
    def __init__(self, name='goblin'):
        super().__init__(name)
        # self.monster_type = self.monsters[randrange(1, 5)]
