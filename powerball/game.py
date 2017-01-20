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