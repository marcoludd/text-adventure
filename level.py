#!/usr/bin/env python
'''creating cool levels'''
import monster
import item
from random import randrange



class Level:
    def __init__(self, ambience='nothing', monster=True, item=True):
        if (monster):
            self.create_monster()
        if (item):
            self.create_item()
        self.ambience = ambience

    def create_monster(self):
        self.monster_ = monster.Monster()

    def create_item(self):
        self.item_ = item.Item()

    def level_description(self):
        description = 'Your are in ' + self.ambience + '\nYou see a ' + self.monster_.monster_type + '\n'
        return description

    def item_description(self):
        item_description = '\nYou see a '+ self.item_.name + ' of ' + self.item_.bonus + '\n'
        return item_description

    levels = {1: 'a dark and damp cave',
              2: 'a deep forest',
              3: 'a secluded garden',
              4: 'a scorching desert',
              5: 'a haunted house'
              }

