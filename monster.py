#!/usr/bin/env python
'''monster class'''
import persona
from random import randrange


class Monster(persona.Persona):
    def __init__(self, name='goblin', growl='uurgh'):
        super().__init__(name)
        self.growl = growl
        #self.monster_type = self.monsters[randrange(1, 5)]

    def growl(self):
        return self.growl

