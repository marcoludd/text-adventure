#!/usr/bin/env python
'''player class'''
import persona


class Player(persona.Persona):
    def __init__(self, name='default_char', job='soldier'):
        super().__init__(name)
        self.job = job

