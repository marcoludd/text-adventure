#!/usr/bin/env python
'''Items'''
from random import randrange


class Item:
    def __init__(self):
        self.name = self.items[randrange(1, 5)]
        self.bonus = self.bonus[randrange(1, 3)]


    items = {1: 'sword',
        2: 'shield',
        3: 'mace',
        4: 'armor',
        5: 'helmet'
    }

    bonus = {1: 'strength',
        2: 'speed',
        3: 'magic'}
