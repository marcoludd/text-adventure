#!/usr/bin/env python
'''The view'''


class View:
    def start(self):
        print('Welcome to the very basic text-adventure game\n')
        print('1: Create Character \n'
              '2: Nothing \n'
              '0: Exit Game \n')
        return int(input('Choice: '))

    def terminate(self):
        print('Farewell adventurer')
