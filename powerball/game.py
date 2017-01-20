#!/usr/bin/env python

from collections import Counter
from .player import Player

class Game:

    def __init__(self, players=None):
        """
        Initialize the game instance.
        players may be initialized by argument or by calling the begin method.
        winning_numbers is initialized with an empty list. It should be populated
        by the generate_winning_numbers method when called.

        :param players (list): list of players
        """

        self.players = list()
        self.winning_numbers = list()

    def add_player(self):
        """
        Create a new player by calling the from_input method of Player class which returns Player instance.
        Add the instance to player list.
        """

        player = Player.from_input()
        self.players.append(player)

    def begin(self):
        """
        Begin the game by calling the add_player to add the first player.
        Keep asking if want to add more players.
        Call add_player till the answer is yes.
        """

        add_more = True

        # since add_more is True, this will ask for first player details by default.
        # further players data depend on user response to add more.

        while add_more:
            self.add_player()

            # True if user enters 'Y' or 'y'. False for any other input.

            add_more = (input("Do you want to add another employee? (y/n) : ").strip().lower() == 'y')

    def display_players(self):
        """
        Print all players data.
        """

        print('\n')

        for player in self.players:
            print(player)

    def display_winning_numbers(self):
        """
        Print the winning numbers if available, otherwise print error message.
        """

        print('\n')

        if self.winning_numbers:
            display_str = "{} {} {} {} {} Powerball: {}".format(*self.winning_numbers)
        else:
            display_str = "Winning numbers are not out yet. Patience!"

        print("Powerball winning number:\n")
        print(display_str)
