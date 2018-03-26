#!/usr/bin/env python
'''The view'''


class View:
    def start_menu(self):
        print('Welcome to the very basic text-adventure game\n')
        print('1: Create Character \n'
              '0: Exit Game \n')
        return int(input('\nChoice: '))
    
    def player_menu(self):
        print('Your journey has started')
        print('e Equipment \n'
              's Stats \n'
              'l Change Level\n')
        return input('')

    def level_menu(self):
        print('Description')
        print('Monster')
        print('Treasure')
        print('Leave')
        
    def terminate(self):
        print('\nFarewell adventurer')

    def ask_name(self):
        return input('\nName: ')

    def ask_job(self):
        return input('\nJob: ')