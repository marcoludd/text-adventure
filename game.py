import player
import level
import item
from random import randrange


class Game:


    items_dict = {1: 'sword',
                  2: 'shield',
                  3: 'mace',
                  4: 'armor',
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
    
    # Later, use as parameters (self, ambience, monster, item)
    def create_level(self):
        ambience = self.ambience_dict[randrange(1, 5)]
        monster = self.monster_dict[randrange(1, 5)]
        item = self.items_dict[randrange(1, 5)]
        self.level_ = level.Level(ambience, monster, item)

    def level_description(self):
        return self.level_.ambience

    def monster_description(self):
        return self.level_.monster

    def item_description(self):
      pass

    def player_name(self):
        return self.player_.name

    def player_job(self):
        return self.player_.job



