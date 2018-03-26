#!/usr/bin/env python
'''Controlling it all'''
import view
import player


class Game:
    def __init__(self):
        self.view = view.View()

    def start_game(self):
        while True:
            choice = self.view.start()
            if choice == 0:
                self.view.terminate()
                break
            if choice == 1:
                player_one = player.Player(self.view.ask_name(),self.view.ask_job())
                print (player_one.name)
                print (player_one.job)

if __name__ == '__main__':
    main = Game()
    main.start_game()