import player
import level
import item
import store
from random import randrange
from random import choice


class Game:

    wins = 0
    last_attack = 0
    last_hit = 0


    items_dict = {1: 'sword',
                  2: 'shield',
                  3: 'mace',
                  4: 'plate armor',
                  5: 'helmet'
                  }

    item_store = {1: 'spear', 
                  2: 'halberd',
                  3: 'glaive',
                  4: 'scythe'}

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
    '''
    Singleton
    '''
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Game, cls).__new__(cls)
            return cls._instance

    def __init__(self):
        self.store_ = store.Store()
        self.fill_store(10)
    
    def create_player(self, name, job):
        self.player_ = player.Player(name, job)
        self.inventory_player = list()
        self.inventory_player.append(item.Item('amulet', 'magic'))
        self.change_equips(0)
        self.wallet = 0
        
    def player_victory(self):
        return self.wins

    def gain_money(self, ammount):
        self.wallet += ammount

    def lose_money(self, ammount):
        self.wallet -= ammount

    def player_wallet(self):
        return self.wallet

    def buy_item(self, number):
        price = self.store_.store_inventory[number].price
        if (self.player_wallet() > price):
            self.lose_money(price)
            self.inventory_player.append(self.store_.store_inventory[number])
            del self.inventory_player[number]
            return 0
        else:
            return 1


    def change_equips(self, number):
        self.equipped_item = self.inventory_player[number]
        # Test if an item was already used
        if (self.equipped_item.used == False):
            bonus = self.equipped_item.bonus
            unit = 1
            if (self.equipped_item.store):
                unit = 2
            if (bonus == 'strength'):
                self.player_.str_mod(unit)
            elif (bonus == 'speed'):
                self.player_.spd_mod(unit)
            elif (bonus == 'magic'):
                self.player_.mag_mod(unit)
            self.equipped_item.used = True
        self.player_.hp_mod()

    '''
        Store
    '''

    def fill_store(self, quantity):
        counter = quantity
        while(counter > 0):
            item_rand = self.items_dict[randrange(1, 5)]
            bonus_item = self.bonus_dict[randrange(1, 3)]
            price_item = randrange(100, 1000)
            self.item_store = item.Item(item_rand, bonus_item, price_item)
            self.item_store.store = True
            self.store_.store_inventory.append(self.item_store)
            counter -= 1

    def store_items(self):
        return self.store_.store_inventory

    '''
        LEVEL
    '''

    def create_level(self):
        ambience = self.ambience_dict[randrange(1, 5)]
        monster = self.monster_dict[randrange(1, 5)]
        item_rand = self.items_dict[randrange(1, 5)]
        bonus_item = self.bonus_dict[randrange(1, 3)]
        self.item_level = item.Item(item_rand, bonus_item)
        self.level_ = level.Level(ambience, monster)

    def level_description(self):
        return self.level_.ambience

    '''
        MONSTER
    '''
    def monster_attack(self):
        return self.level_.monster.attack()

    def monster_description(self):
        return self.level_.monster.name

    def monster_hp(self):
        return self.level_.monster.hp

    def monster_name(self):
        return self.level_.monster.name

    def monster_damage(self, number):
        return self.level_.monster.damage(number)

    def monster_alive(self):
        return self.level_.monster.alive 


    # ITEM
    def take_item(self):
        if (not self.level_.monster.alive):
            if (self.item_level.name != 'nothing'):
                self.inventory_player.append(self.item_level)
                self.item_level = item.Item('nothing', 'nothing')
               
    def item_description(self):
        return self.item_level.name

    # PLAYER

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
    
    def player_attack(self):
        return self.player_.attack()
    
    def player_damage(self, number):
        return self.player_.damage(number)
    
    def player_alive(self):
        return self.player_.is_alive()
    '''
    Attack Monster
    ''' 
    def attack_monster(self):
        self.last_attack = 0
        self.last_hit = 0
        self.last_attack = randrange(0, self.player_attack())
        self.monster_damage(self.last_attack)
        if (self.monster_alive()):
            if (choice([True, False])):
                self.last_hit = randrange(0, self.monster_attack())
                self.player_damage(self.last_hit)
                if (not self.player_.is_alive()):
                    return 3
        else:
            self.wins += 1
            self.drop_coins(self.player_hp())
            self.player_.hp_mod()

            return 4

    def drop_coins(self, ammount):
        self.wallet += int(10/(0.01 * ammount))

