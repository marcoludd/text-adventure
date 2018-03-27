#!/usr/bin/env python
'''monster class'''
import persona

class Monster(persona.Persona):
    def __init__(self, name='goblin', growl='uurgh'):
        super().__init__(name)
        self.growl = growl


    def growl(self):
        return self.growl
