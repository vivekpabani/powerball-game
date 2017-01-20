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

    @staticmethod
    def _get_name(name_type):
        """
        Get the name of name_type from the user and verify.

        :param name_type (str): The type of name - 'first' or 'last' - to be used in prompt.

        :return (str): valid user entered name.
        """

        name = ''

        # while the user entered name is not valid, ask for the name.

        while not name:
            name = input("Enter your {} name: ".format(name_type)).strip()

            if not name:
                print("Invalid {} name. Please try again.".format(name_type))

        return name


