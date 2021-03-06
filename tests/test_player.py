#!/usr/bin/env python

"""
Tests for the Player class methods.
"""

__author__ = "vivek"


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

    def test_is_valid_number_with_valid_wb_15(self):

        number = 15
        number_list = [10, 20]

        valid = Player.is_valid_number(number, number_list)

        assert valid == True

    def test_is_valid_number_with_valid_wb_1_lower_limit(self):

        number = 1
        number_list = [10, 20]

        valid = Player.is_valid_number(number, number_list)

        assert valid == True

    def test_is_valid_number_with_valid_wb_69_upper_limit(self):

        number = 69
        number_list = [10, 20]

        valid = Player.is_valid_number(number, number_list)

        assert valid == True

    def test_is_valid_number_with_valid_pb_15(self):

        number = 15
        number_list = [10, 20, 30, 40, 50]

        valid = Player.is_valid_number(number, number_list)

        assert valid == True

    def test_is_valid_number_with_valid_pb_1_lower_limit(self):

        number = 1
        number_list = [10, 20, 30, 40, 50]

        valid = Player.is_valid_number(number, number_list)

        assert valid == True

    def test_is_valid_number_with_valid_pb_26_upper_limit(self):

        number = 26
        number_list = [10, 20, 30, 40, 50]

        valid = Player.is_valid_number(number, number_list)

        assert valid == True

    def test_is_valid_number_with_invalid_wb_15_repeated(self):

        number = 15
        number_list = [10, 15]

        valid = Player.is_valid_number(number, number_list)

        assert valid == False

    def test_is_valid_number_with_invalid_wb_X_not_a_number(self):

        number = 'X'
        number_list = [10, 15]

        valid = Player.is_valid_number(number, number_list)

        assert valid == False

    def test_is_valid_number_with_invalid_wb_0_lower_then_limit(self):

        number = 0
        number_list = [10, 15]

        valid = Player.is_valid_number(number, number_list)

        assert valid == False

    def test_is_valid_number_with_invalid_wb_70_higher_then_limit(self):

        number = 70
        number_list = [10, 15]

        valid = Player.is_valid_number(number, number_list)

        assert valid == False

    def test_is_valid_number_with_invalid_pb_0_lower_then_limit(self):

        number = 0
        number_list = [10, 15, 20, 25, 30]

        valid = Player.is_valid_number(number, number_list)

        assert valid == False

    def test_is_valid_number_with_invalid_pb_27_higher_then_limit(self):

        number = 27
        number_list = [10, 15, 20, 25, 30]

        valid = Player.is_valid_number(number, number_list)

        assert valid == False

    def test_get_numbers_with_all_valid_numbers(self):

        input_numbers = [2, 5, 8, 13, 45, 24]

        with mock.patch('builtins.input', side_effect=input_numbers):
            numbers = Player._get_numbers()

        assert numbers == input_numbers

    def test_get_numbers_with_invalid_numbers_X_not_a_number(self):

        input_numbers = [2, 5, 15, 8, 'X', 13, 24]

        with mock.patch('builtins.input', side_effect=input_numbers):
            numbers = Player._get_numbers()

        expected_output_numbers = [2, 5, 15, 8, 13, 24]

        assert numbers == expected_output_numbers

    def test_get_numbers_with_invalid_numbers_15_repeated(self):

        input_numbers = [2, 5, 15, 8, 15, 13, 24]

        # more than 5 numbers are provided as mock input, since initial invalid
        # inputs will result in next promt until valid value is entered.

        with mock.patch('builtins.input', side_effect=input_numbers):
            numbers = Player._get_numbers()

        expected_output_numbers = [2, 5, 15, 8, 13, 24]

        assert numbers == expected_output_numbers

    def test_get_numbers_with_invalid_numbers_100_out_of_wb_range(self):

        input_numbers = [2, 5, 15, 8, 100, 13, 24]

        # more than 5 numbers are provided as mock input, since initial invalid
        # inputs will result in next promt until valid value is entered.

        with mock.patch('builtins.input', side_effect=input_numbers):
            numbers = Player._get_numbers()

        expected_output_numbers = [2, 5, 15, 8, 13, 24]

        assert numbers == expected_output_numbers

    def test_get_numbers_with_invalid_numbers_50_out_of_pb_range(self):

        input_numbers = [2, 5, 15, 8, 13, 50, 24]

        # more than 5 numbers are provided as mock input, since initial invalid
        # inputs will result in next promt until valid value is entered.

        with mock.patch('builtins.input', side_effect=input_numbers):
            numbers = Player._get_numbers()

        expected_output_numbers = [2, 5, 15, 8, 13, 24]

        assert numbers == expected_output_numbers

    def test_from_input_with_all_valid_inputs(self):

        input_names = ['Foo', 'Bar']
        input_numbers = [2, 5, 8, 13, 45, 24]

        input_data = input_names + input_numbers

        with mock.patch('builtins.input', side_effect=input_data):
            player = Player.from_input()

        assert player.first_name == input_names[0]
        assert player.last_name == input_names[1]
        assert player.numbers == input_numbers

    def test_from_input_with_invalid_names_blank_spaces_newline(self):

        input_names = ['', '   ', '\n', 'Foo', '', '  ', '\n', 'Bar']
        input_numbers = [2, 5, 8, 13, 45, 24]

        input_data = input_names + input_numbers

        with mock.patch('builtins.input', side_effect=input_data):
            player = Player.from_input()

        expected_output_names = ['Foo', 'Bar']
        expected_output_numbers = [2, 5, 8, 13, 45, 24]

        assert player.first_name == expected_output_names[0]
        assert player.last_name == expected_output_names[1]
        assert player.numbers == expected_output_numbers

    def test_from_input_with_invalid_numbers_repeated_outoflimit_notanumber(self):

        input_names = ['Foo', 'Bar']
        input_numbers = [2, -1,  5,  2, 'X', 100, 8, 13, 45, 30, 70, 24]

        input_data = input_names + input_numbers

        with mock.patch('builtins.input', side_effect=input_data):
            player = Player.from_input()

        expected_output_names = ['Foo', 'Bar']
        expected_output_numbers = [2, 5, 8, 13, 45, 24]

        assert player.first_name == expected_output_names[0]
        assert player.last_name == expected_output_names[1]
        assert player.numbers == expected_output_numbers

    def test_is_valid_player_with_all_valid_arguments(self):

        names = ['Foo', 'Bar']
        numbers = [2, 5, 8, 13, 45, 24]

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == True

    def test_is_valid_player_with_no_arguments(self):

        player = Player()

        assert player.is_valid_player() == False

    def test_is_valid_player_with_invalid_arguments_names_none(self):

        names = ['', '']
        numbers = [2, 5, 8, 13, 45, 24]

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == False

    def test_is_valid_player_with_invalid_arguments_numbers_none(self):

        names = ['Foo', 'Bar']
        numbers = []

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == False

    def test_is_valid_player_with_invalid_arguments_numbers_repeated(self):

        names = ['Foo', 'Bar']
        numbers = [2, 5, 8, 5, 45, 24]

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == False

    def test_is_valid_player_with_invalid_arguments_numbers_out_of_range(self):

        names = ['Foo', 'Bar']
        numbers = [2, 5, 8, 100, 45, 24]

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == False

    def test_is_valid_player_with_invalid_arguments_numbers_notanumber(self):

        names = ['Foo', 'Bar']
        numbers = [2, 5, 8, 'X', 45, 24]

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == False

    def test_is_valid_player_with_invalid_arguments_numbers_count_less_than_6(self):

        names = ['Foo', 'Bar']
        numbers = [2, 5, 8, 24]

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == False

    def test_is_valid_player_with_invalid_arguments_numbers_count_more_than_6(self):

        names = ['Foo', 'Bar']
        numbers = [2, 5, 8, 10, 15, 30, 40, 45, 24]

        player = Player(names[0], names[1], numbers)

        assert player.is_valid_player() == False
