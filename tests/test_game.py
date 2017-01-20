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
