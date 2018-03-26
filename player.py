#!/usr/bin/env python
'''player class'''
import persona

class Player(persona.Persona):


    def __init__(self, name='default_char', strenght=1, speed=1, magic=0, job='soldier'):
        super().__init__(name, strenght, speed, magic)
        self.job = job

'''#tests
player1 = Player('playerone',4,2,3,'warrior')
print (player1.get_name())
print (player1.get_strenght())
'''