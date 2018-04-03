#!/usr/bin/env python
'''creating cool levels'''
import monster
import item
from random import randrange



class Level:
    def __init__(self, ambience='nothing', monster=True, item=True):
        #if (monster):
         #   self.create_monster(monster)
        #if (item):
          #  self.create_item()
        self.ambience = ambience
        self.monster = monster
        self.item = item

    def create_monster(self, monster_name):
        self.monster_ = monster.Monster(monster_name)

    def create_item(self):
        self.item_ = item.Item()

    def level_description(self):
        description = 'Your are in ' + self.ambience + '\nYou see a ' + self.monster_.name + '\n'
        return description

    def item_description(self):
        item_description = '\nYou see a '+ self.item_.name + ' of ' + self.item_.bonus + '\n'
        return item_description



