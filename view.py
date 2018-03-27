#!/usr/bin/env python
'''The view'''


class View:
    def welcome(self):
        print('Welcome to the very basic text-adventure game\n')

    def start_menu(self):
        print('1: Create Character \n'
              '0: Exit Game \n')
        return int(input('\nChoice: '))
    
    def level_menu(self):
        print('Your journey has started')
        print('1: Stats || '
              '2: Level Description || '
              '3: Change Level || '
              '0: Exit Game')
        return int(input('\nChoice: '))

    def terminate(self):
        print('\nFarewell adventurer')

    def ask_name(self):
        return input('\nName: ')

    def ask_job(self):
        return input('\nJob: ')

    def player_stats(self, name, job):
        print('Name: '+ name +'\n'
              'Job:'+ job +'\n')