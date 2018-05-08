import player
import level
import item
from random import randrange


class Game:


    items_dict = {1: 'sword',
                  2: 'shield',
                  3: 'mace',
                  4: 'plate armor',
                  5: 'helmet'
                  }

    monster_dict = {1: 'goblin',
                   2: 'skeleton',
                   3: 'dragon',
                   4: 'golem',
                   5: 'gargoyle'
                  }

    bonus_dict = {1: 'strength',
                  2: 'speed',
                  3: 'magic'
                  }

    ambience_dict = {1: 'a dark and damp cave',
                     2: 'a deep forest',
                     3: 'a secluded garden',
                     4: 'a scorching desert',
                     5: 'a haunted house'
                     }


    def create_player(self, name, job):
        self.player_ = player.Player(name, job)
        self.inventory_player = list()

    # Later, use as parameters (self, ambience, monster, item)
    def create_level(self):
        ambience = self.ambience_dict[randrange(1, 5)]
        monster = self.monster_dict[randrange(1, 5)]
        item_rand = self.items_dict[randrange(1, 5)]
        bonus_item = self.bonus_dict[randrange(1, 3)]
        self.item_level = item.Item(item_rand, bonus_item)
        self.level_ = level.Level(ambience, monster, self.item_level)

    def take_item(self):
        self.inventory_player.append(self.item_level)

    def add_inventory(self, Item):
        self.inventory_player.append(Item)

    def check_inventory(self):
        for f in self.inventory_player:
            print (f.name)

    def level_description(self):
        return self.level_.ambience

    def monster_description(self):
        return self.level_.monster

    def item_description(self):
        return self.item_level.name

    def player_name(self):
        return self.player_.name

    def player_job(self):
        return self.player_.job



