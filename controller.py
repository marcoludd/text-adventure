#!/usr/bin/env python
'''Controlling it all'''
import view
import game
import os
import sys
from random import randrange

class Controller:
    def __init__(self):
        self.view = view.View()
        self.game = game.Game()
        self.clear_screen()

    # Clear terminal window
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit_game(self):
        self.clear_screen()
        self.view.terminate()
        sys.exit()

    def player_stats(self):
        self.view.player_stats(self.game.player_name,self.game.player_job)


    def starter_level(self):
        self.clear_screen()
        self.view.start_journey()
        #self.create_level()
        self.game.create_level()
        while True:
            self.level_menu_choice(self.view.level_menu())

    def level_menu_choice(self, choice):
        if choice == 0:
            self.exit_game()
        elif choice == 1:
            self.player_stats()
        elif choice == 2:
            #self.view.print_message(self.level_.level_description())
            self.view.print_message(self.game.level_description())
        elif choice == 4:
            #self.view.print_message(self.level_.item_description())
            self.view.print_message(self.game.item_description())
        elif choice == 3:
            #if (self.view.choose_level() == randrange(1,4)):
            #    self.create_level()
            self.create_level()

    def start_game(self):
        self.view.welcome()
        self.start_menu_choice(self.view.start_menu())

    def start_menu_choice(self, choice):
        if choice == 0:
            self.exit_game()
        elif choice == 1:
            #self.create_player()
            self.game.create_player(self.view.ask_name(), self.view.ask_job())
            self.starter_level()

    def create_player(self):
        self.player_ = player.Player(self.view.ask_name(),self.view.ask_job())
    
    def create_level(self):
        self.level_ = level.Level()


if __name__ == '__main__':
    main = Controller()
    main.start_game()