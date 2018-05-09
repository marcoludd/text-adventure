#!/usr/bin/env python
'''Controlling it all'''
import view
import game
import os
import sys
import combat

class Controller:
    def __init__(self):
        self.view = view.View()
        self.game = game.Game()
        self.clear_screen()

    # Clear terminal - works on windows and linux
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Exit game
    def exit_game(self):
        self.clear_screen()
        self.view.terminate()
        sys.exit()

    # Start game, by welcoming the player and showing the first menu 
    def start_game(self):
        self.view.welcome()
        self.start_menu_choice(self.view.start_menu())  

    def start_menu_choice(self, choice):
        if choice == 0:
            self.exit_game()
        elif choice == 1:
            self.create_player()
            self.starter_level()

    # After creating the character, this is the default menu 
    def starter_level(self):
        self.clear_screen()
        self.view.start_journey()
        self.game.create_level()
        while True:
            self.level_menu_choice(self.view.level_menu())

    # The default choices
    # TODO change order
    def level_menu_choice(self, choice):
        self.clear_screen()
        if choice == 0:
            self.exit_game()
        elif choice == 1:
            self.player_stats()
        elif choice == 2:
            self.level_description()
        elif choice == 4:
            self.item_description()
            self.take_item()
        elif choice == 3:
            self.create_level()
            self.clear_screen()
            self.level_description()
        elif choice == 5:
            self.change_equips()
        elif choice == 6:
            self.attack_monster()

    def attack_monster():
        self.game.attack_monster()
            
    def create_player(self):
        self.game.create_player(self.view.ask_name(), self.view.ask_job())

    def create_level(self):
        self.game.create_level()

    def level_description(self):
        self.view.print_ambience(self.game.level_description())
        self.view.print_monster(self.game.monster_description())
        self.view.print_monster_hp(self.game.monster_hp())
        
    def item_description(self):
        self.view.print_item(self.game.item_description())
 
    # Return player stats
    def player_stats(self):
        name = self.game.player_name()
        job = self.game.player_job()
        hp = str(self.game.player_hp())
        strength = str(self.game.player_str())
        speed = str(self.game.player_spd())
        magic = str(self.game.player_mag())
        self.view.player_stats(name, job, hp, strength, speed, magic)
        self.view.show_equip(self.game.equipped_item.name, self.game.equipped_item.bonus)
        for equipment in self.game.inventory_player:
            self.view.print_inventory(equipment.name, equipment.bonus)

    def change_equips(self):
        for i, equipment in enumerate(self.game.inventory_player):
            self.view.print_equips(str(i), equipment.name, equipment.bonus)
        self.game.change_equips(self.view.choose_equips())

    def take_item(self):
        self.game.take_item()

if __name__ == '__main__':
    main = Controller()
    main.start_game()
