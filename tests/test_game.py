#!/usr/bin/python

try:
    import mock
except ImportError:
    from unittest import mock

from .context import powerball

from powerball.game import Game
from powerball.player import Player
