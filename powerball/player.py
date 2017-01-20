#!/usr/bin/env python

"""
The Player class of the application represents the player of the game.
"""


class Player:

    def __init__(self, first_name = None, last_name = None, numbers = None):
        """
        Initiate the player instance.
        The first name, last name and numbers can be provided as arguments here,
        or by the user input calling the from_input method.

        :param first_name (str) (default: None): first name of the player.
        :param last_name (str) (default: None): last name of the player.
        :param numbers (list) (default: None): favorite numbers of the player
                                including the white ball numbers and power ball numbers.
        """

        self.first_name = first_name
        self.last_name = last_name

        # accept the numbers if it's a list, otherwise create a new list.

        if numbers and isinstance(numbers, list):
            self.numbers = numbers
        else:
            self.numbers = list()

