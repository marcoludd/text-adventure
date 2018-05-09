import player
import level
import item
from random import randrange
from random import choice


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
        self.inventory_player.append(item.Item('amulet', 'magic'))
        self.change_equips(0)


    def change_equips(self, number):
        self.equipped_item = self.inventory_player[number]
        bonus = self.equipped_item.bonus
        if (bonus == 'strength'):
            self.player_.str_mod(1)
        elif (bonus == 'speed'):
            self.player_.spd_mod(1)
        elif (bonus == 'magic'):
            self.player_.mag_mod(1)
        self.player_.hp_mod()
        
    # Later, use as parameters (self, ambience, monster, item)
    def create_level(self):
        ambience = self.ambience_dict[randrange(1, 5)]
        #monster = self.monster_dict[randrange(1, 5)]
        item_rand = self.items_dict[randrange(1, 5)]
        bonus_item = self.bonus_dict[randrange(1, 3)]
        monster_bool = choice([True, False])
        self.item_level = item.Item(item_rand, bonus_item)
        self.level_ = level.Level(ambience, monster_bool, self.item_level)

    def take_item(self):
        if (self.item_level.name != 'nothing'):
            self.inventory_player.append(self.item_level)
            self.item_level = item.Item('nothing', 'nothing')

    def level_description(self):
        return self.level_.ambience

    def monster_description(self):
        return self.level_.monster.name

    def monster_hp(self):
        return self.level_.monster.hp

    def item_description(self):
        return self.item_level.name

    def player_name(self):
        return self.player_.name

    def player_job(self):
        return self.player_.job

    def player_str(self):
        return self.player_.strength

    def player_spd(self):
        return self.player_.speed

    def player_mag(self):
        return self.player_.magic
    
    def player_hp(self):
        return self.player_.hp
  
    def attack_monster()
        level_.monster.hp -= self.player_attack()
        if (monster_alive())
            if (choice([True, False])):
                player_damage(level_.monster.attack())
    
