#!/usr/bin/env python
'''The view'''


class View:
    def welcome(self):
        print('Welcome to the very basic text-adventure game\n')

    def start_journey(self):
        print('Your journey has started\n')

    def start_menu(self):
        print('1: Create Character \n'
              '0: Exit Game \n')
        return int(input('\nChoice: '))

    def level_menu(self):
        print('1: Stats || '
              '2: Level Description || '
              '3: Change Level || '
              '4: Explore room || '
              '5: Change equipment ||'
              '6: Attack monster ||'
              '7: Visit store ||'
              '0: Exit Game')
        return int(input('\nChoice: '))

    def terminate(self):
        print('\nFarewell adventurer')

    def ask_name(self):
        return input('\nName: ')

    def ask_job(self):
        return input('\nJob: ')

    def print_message(self, message):
        print (message)

    def player_stats(self, name, job, hp, strength, speed, magic, coins):
        print('Name: '+ name + '\n'
              'Job:'+ job + '\n'
              'HP:'+ hp + '\n'
              'Strength:' + strength + '\n'
              'Speed:' + speed + '\n'
              'Magic:' + magic + '\n'
              'Coins:' + coins + '\n')

    def print_ambience(self, ambience):
        print('\nYou are in a ' + ambience)

    def print_monster(self, monster):
        print('\nYou see a ' + monster + '\n')

    def print_monster_hp(self, hp):
        print('\nIt has ' + hp + ' Hit Points')

    def print_item(self, item):
        print('You found a ' + item)

    def print_inventory(self, name, bonus):
        print('You have a ' + name + ' of ' + bonus + '\n')

    def print_equips(self, number, name, bonus):
        print(number + ' ' + name + ' of ' + bonus + '\n')

    def choose_equips(self):
        return int(input('Choose your equipment: '))

    def show_equip(self, name, bonus):
        print('You are using the ' + name + ' of ' + bonus + '\n')

    def combat_attack(self, player_attack, monster_name, monster_hp):
        print("You inflicted " + player_attack +
              " points of damage in the " + monster_name +
              " and it's down to " + monster_hp + " Hit Points\n")

    def combat_damage(self, monster_attack, monster_name, player_hp):
        print("\nThe " + monster_name + " inflicted you with " + monster_attack +
              " points of damage, and your life is down to " + player_hp + " Hit Points\n")

    def lost_combat(self):
        print("\nYou have died. May the Gods have mercy on your soul\n")

    def finish_game(self):
        print("\nCongratulations! You have found the way out of the dungeon!")
        print("\nMay the Gods guide your path\n")

    def monster_defeated(self, monster_name):
        print('The ' + monster_name + " is defeated\n")

    def store_closed(self):
        print('\nDefeat the monster first!\n')

    def store_open(self):
        print('\nWelcome! Take a look at these items...\n')

    def show_store(self, number, name, bonus, price):
        print(number + ' ' + name + ' of ' + bonus + ' price: ' + price + 'coins \n')

    def choice_store(self):
        return int(input('\nExit: 10 \nChoose your item: \n '))
