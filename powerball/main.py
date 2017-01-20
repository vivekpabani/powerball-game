#!/usr/bin/python

from .game import Game
from .player import Player


def main():

    print('\n')

    game = Game()
    game.begin()
    game.generate_winning_numbers()
    game.display_players()
    game.display_winning_numbers()

    print('\n')

if __name__ == "__main__":

    main()
