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

            add_more = (input("\nDo you want to add another player? (y for yes/any key for no) : ").strip().lower() == 'y')

    def generate_winning_numbers(self):
        """
        Generate the winning number based on the players numbers.
        The 5 white balls are generated from the top 5 white ball numbers entered by all players.
        The 6th power ball is generated from the maximum occuring user power balls.
        If any of those choices have ties, they are resolved randomly.
        Add the winning numbers to the winning_numbers.
        """

        # Players added by the begin or add_player method are by default verified.
        # In case the players are initialized at the time of game instance creation,
        # we should check for player validity before generating the winning numbers.

        for player in self.players:
            if not isinstance(player, Player) or not player.is_valid_player():
                print("Some or all players are invalid.")
                return

        # get the list of white balls and power balls entered by all players.
        wb_nums = self.get_white_ball_numbers()
        pb_nums = self.get_power_ball_numbers()

        # Counter returns the counter object with count of each number in the list.
        # Counter.most_common(i) retuns the maximum occuring top i numbers from the list.
        # In case of ties between counts, most_common returns arbitary number,
        # which fulfills our condition of resolving the ties by choosing a random number.
        # so no extra check required for ties between counts.

        top_five_wb = [item[0] for item in Counter(wb_nums).most_common(5)]
        top_pb = Counter(pb_nums).most_common(1)[0][0]

        # add the winning numbers to the list.

        self.winning_numbers.extend(top_five_wb)
        self.winning_numbers.append(top_pb)

    def get_white_ball_numbers(self):
        """
        Get the white ball numbers from all the players and return as a list.

        :return (list): list of white ball numbers extracted from all the players numbers.
        """

        numbers = list()

        for player in self.players:
            numbers.extend(player.numbers[:-1])

        return numbers

    def get_power_ball_numbers(self):
        """
        Get the power ball numbers from all the players and return as a list.

        :return (list): list of power ball numbers extracted from all the players numbers.
        """

        numbers = list()

        for player in self.players:
            numbers.append(player.numbers[-1])

        return numbers

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
