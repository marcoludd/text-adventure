#!/usr/bin/env python
'''Items'''


class Item:
    def __init__(self, name, bonus, price=0):
        self.name = name
        self.bonus = bonus
        self.used = False
        self.store = False
        self.price = price
