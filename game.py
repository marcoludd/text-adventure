import player
import level
import item
from random import randrange


class Game:
    def __init__(self):
        pass

    def create_player(self):
        self.player_ = player.Player(self.view.ask_name(),self.view.ask_job())
    
    def create_level(self):
        self.level_ = level.Level() 

    def player_name(self):
        return player_.name

    def player_job(self):
        return player_.job


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
        3: 'magic'}
