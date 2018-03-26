#!/usr/bin/env python
'''Controlling it all'''
import view
import character
import player


class Game:
    def __init__(self):
        self.view = view.View()

    def start_game(self):

        while True:
            choice = self.view.start()
            if choice == 2:
                self.view.terminate()
            break
            if choice == 1:
                # if opcao == criar personag
                #player.create()


if __name__ == 'main':
    main = Game()
    main.start_game()
