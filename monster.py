#!/usr/bin/env python
'''monster class'''
import persona
from random import randrange


class Monster(persona.Persona):
    def __init__(self, name='joey', growl='uurgh'):
        super().__init__(name)
        self.growl = growl
        self.monster_type = self.monsters[randrange(1, 5)]

    def growl(self):
        return self.growl

    monsters = {1: 'goblin',
                2: 'skeleton',
                3: 'ghost',
                4: 'zombie',
                5: 'crododile'
                }

