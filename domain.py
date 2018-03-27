#!/usr/bin/env python
'''Controlling it all'''
import view
import player
import os
import sys


class Game:
    def __init__(self):
        self.view = view.View()

    # Clear terminal window
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit_game(self):
        self.clear_screen()
        self.view.terminate()
        sys.exit()

    def starter_room(self):
        while True:
            main.clear_screen()
            choice = self.view.level_menu()
            if choice == 0:
                self.exit_game()
    
    def start_game(self):
        self.view.welcome()
        while True:
            main.clear_screen()
            choice = self.view.start_menu()
            if choice == 0:
                self.exit_game()
            if choice == 1:
                main.create_player()
                main.starter_room()


    def create_player(self):
        player_ = player.Player(self.view.ask_name(),self.view.ask_job())

if __name__ == '__main__':
    main = Game()
    main.start_game()