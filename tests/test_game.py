#!/usr/bin/python

try:
    import mock
except ImportError:
    from unittest import mock

from .context import powerball

from powerball.game import Game
from powerball.player import Player


class TestGameClass:

    def test_init_instance_type(self):

        game = Game()
        assert isinstance(game, Game) == True

    def test_add_player(self):

        game = Game()

        assert len(game.players) == 0

        input_names = ['Foo', 'Bar']
        input_numbers = [2, 5, 8, 13, 45, 24]

        input_data = input_names + input_numbers

        with mock.patch('builtins.input', side_effect=input_data):
            game.add_player()

        assert len(game.players) == 1
        player = game.players[0]

        assert player.first_name == input_names[0]
        assert player.last_name == input_names[1]
        assert player.numbers == input_numbers

    def test_begin_with_adding_3_players(self):

        game = Game()

        assert len(game.players) == 0

        input_names = ['Foo', 'Bar']
        input_numbers = [2, 5, 8, 13, 45, 24]

        input_data = input_names + input_numbers

        res_y = ['y']
        res_n = ['n']

        three_player_data = input_data + res_y + input_data + res_y + input_data + res_n

        with mock.patch('builtins.input', side_effect=three_player_data):
            game.begin()

        assert len(game.players) == 3

    def test_generate_winning_numbers_4_players_no_tie(self):

        game = Game()

        input_names_1 = ['Foo1', 'Bar1']
        input_numbers_1 = [2, 5, 8, 33, 25, 24]
        input_data_1 = input_names_1 + input_numbers_1

        input_names_2 = ['Foo2', 'Bar2']
        input_numbers_2 = [2, 5, 8, 33, 35, 18]
        input_data_2 = input_names_2 + input_numbers_2

        input_names_3 = ['Foo3', 'Bar3']
        input_numbers_3 = [10, 5, 8, 13, 45, 15]
        input_data_3 = input_names_3 + input_numbers_3

        input_names_4 = ['Foo4', 'Bar4']
        input_numbers_4 = [20, 5, 8, 13, 55, 24]
        input_data_4 = input_names_4 + input_numbers_4

        res_y = ['y']
        res_n = ['n']

        four_player_data = input_data_1 + res_y + input_data_2 + res_y + input_data_3 + res_y + input_data_4 + res_n

        with mock.patch('builtins.input', side_effect=four_player_data):
            game.begin()

        game.generate_winning_numbers()

        expected_winning_numbers = [5, 8, 2, 13, 33, 24]
        winning_numbers = game.winning_numbers

        assert len(winning_numbers) == 6
        assert sorted(winning_numbers[0:5]) == sorted(expected_winning_numbers[0:5])
        assert winning_numbers[5] == expected_winning_numbers[5]
