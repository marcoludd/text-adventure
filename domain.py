#!/usr/bin/env python
'''Controlling it all'''
import view
#import character
#import player


class Game:
    def __init__(self):
        self.view = view.View()

    def start_game(self):
        while True:
            choice = self.view.start()
            if choice == 0:
                self.view.terminate()
                break
            print('escolheu')
            


if __name__ == "__main__":
    main = Game()
    main.start_game()
