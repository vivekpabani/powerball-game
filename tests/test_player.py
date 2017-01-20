#!/usr/bin/python

try:
    import mock
except ImportError:
    from unittest import mock

from .context import powerball
from powerball.player import Player


class TestPlayerClass:

    def test_init_with_all_arguments_none(self):

        player = Player()

        assert player.first_name == None
        assert player.last_name == None
        assert player.numbers == []

    def test_init_with_all_arguments_not_none(self):

        first_name = "Foo"
        last_name = "Bar"
        numbers = [1, 2, 3, 4, 5, 6]

        player = Player(first_name, last_name, numbers)

        assert player.first_name == first_name
        assert player.last_name == last_name
        assert player.numbers == numbers

    @mock.patch('builtins.input', side_effect=['Foo'])
    def test_get_name_with_valid_input_foo_non_blank(self, input):
    
        name = Player._get_name('name_type')
        assert name == 'Foo'
    
    @mock.patch('builtins.input', side_effect=['', '   ', '\n', 'Foo'])
    def test_get_name_with_invalid_inputs_blank_spaces_newline(self, input):
        """
        multiple inputs are provided, since initial invalid
        inputs will result in next promt until valid value is entered.
        """

        name = Player._get_name('name_type')
        assert name == 'Foo'
