import player
import level
import item
from random import randrange


class Game:
    def __init__(self):
        pass

    dict_monster = {1: 'goblin',
                    2: 'skeleton',
                    3: 'ghost',
                    4: 'zombie',
                    5: 'crododile'
                    }

    dict_items = {1: 'sword',
                  2: 'shield',
                  3: 'mace',
                  4: 'armor',
                  5: 'helmet'
                  }

    dict_bonus = {1: 'strength',
                  2: 'speed',
                  3: 'magic'
                  }

    dict_ambience = {1: 'a dark and damp cave',
                     2: 'a deep forest',
                     3: 'a secluded garden',
                     4: 'a scorching desert',
                     5: 'a haunted house'
                     }


    def create_player(self, name, job):
        self.player_ = player.Player(name, job)
    
    def create_level(self, ambience, monster, item):
        self.level_ = level.Level(dict_ambience[randrange(1,5)], dict_monster[randrange(1,5)], dict_items[randrange(1,5)]) 

    def player_name(self):
        return player_.name

    def player_job(self):
        return player_.job



