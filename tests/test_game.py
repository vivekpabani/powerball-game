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
