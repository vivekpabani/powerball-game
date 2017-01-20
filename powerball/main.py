#!/usr/bin/env python

"""
The main script to run the powerball game simulation.
"""

__author__ = "vivek"


from .game import Game
from .player import Player


def main():

    # The game simulation is done with following steps:
    #
    # 1. Create a game instance with no players.
    # 2. Invoke the begin method, which asks for player data and 
    #    favorite numbers until stopped.
    # 3. Once players data is entered, invoke the method to generate 
    #    winning number.
    # 4. Display players data and winning numbers. 

    print('\n')

    game = Game()
    game.begin()
    game.generate_winning_numbers()
    game.display_players()
    game.display_winning_numbers()

    print('\n')

if __name__ == "__main__":

    main()
