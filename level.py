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


