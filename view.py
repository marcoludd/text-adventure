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

    def choose_level(self):
        print ('Choose your destiny:\n'
               '1: North || 2: South || 3: East || 4: West')
        return int(input('\nChoice: '))

    def player_stats(self, name, job, hp, strength, speed, magic):
        print('Name: '+ name + '\n'
              'Job:'+ job + '\n'
              'HP:'+ hp + '\n'
              'Strength:' + strength + '\n'
              'Speed:' + speed + '\n'
              'Magic:' + magic + '\n')

    def print_ambience(self, ambience):
        print('\nYou are in a ' + ambience)

    def print_monster(self, monster):
        print('\nYou see a ' + monster + '\n')

    def print_monster_hp(self, hp):
        print('\nIt has ' + hp + 'Hit Points')

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
