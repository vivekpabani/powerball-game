#!/usr/bin/env python

"""
The Player class of the application represents the player of the game.
"""


class Player:
    """
    Player class for the powerball game.
    """

    def __init__(self, first_name=None, last_name=None, numbers=None):
        """
        Initiate the player instance.
        The first name, last name and numbers can be provided as arguments here,
        or by the user input calling the from_input method.

        :param first_name (str) (default: None): first name of the player.
        :param last_name (str) (default: None): last name of the player.
        :param numbers (list) (default: None): favorite numbers of the player
                       ncluding the white ball numbers and power ball numbers.
        """

        self.first_name = first_name
        self.last_name = last_name

        # accept the numbers if it's a list, otherwise create a new list.

        if numbers and isinstance(numbers, list):
            self.numbers = numbers
        else:
            self.numbers = list()

    @classmethod
    def from_input(cls):
        """
        A class method to create an instance of Player with the user inputs for the
        attributes. Get first, last name and numbers from user by calling respective methods.

        :return (Player): an instance of Player class with user entered attributes.
        """

        first_name = cls._get_name("first")
        last_name = cls._get_name("last")
        numbers = cls._get_numbers()

        return cls(first_name, last_name, numbers)

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

    @staticmethod
    def _get_numbers():
        """
        Get the six favorite numbers from the user and verify.

        :return (list): list of valid numbers entered by user.
        """

        numbers = list()

        # dictionary of the number input prompts based on-
        # which numbered ball, valid range and exclude list.

        display_dict = dict([(1, "Select 1st # (1 thru 69): "),
                             (2, "Select 2nd # (1 thru 69 excluding {}): "),
                             (3, "Select 3rd # (1 thru 69 excluding {} and {}): "),
                             (4, "Select 4th # (1 thru 69 excluding {}, {}, and {}): "),
                             (5, "Select 5th # (1 thru 69 excluding {}, {}, {}, and {}): "),
                             (6, "Select Power Ball # (1 thru 26): ")])

        # get six numbers by asking user for next number
        # and validate each number before adding to final list.

        for i in range(1, 7):

            valid = False

            # ask for current number till a valid number is not entered.

            while not valid:

                display_string = display_dict[i].format(*numbers)

                # if number is not a numeric, raise ValueError.
                # if numeric, check for validity.

                try:
                    next_number = int(input(display_string))
                    valid = Player.is_valid_number(next_number, numbers)

                    if not valid:
                        print("Number not allowed. Please try again.")

                except ValueError:
                    print("Invalid input. Please try again.")

            # a valid number is added to the numbers list.

            numbers.append(next_number)

        return numbers

    @staticmethod
    def is_valid_number(number, number_list):
        """
        Check if current number is valid based on current index and state of number_list.
        Invalid in cases:
        1. not a numeric value.
        2. out of range based on which kind of ball.
        3. repeated white ball number.

        :param number (int): the latest number to be checked.
        :param number_list (list): the list of valid numbers added so far.

        :return (bool): True if the number is valid. False otherwise.
        """

        white_ball_max = 69
        power_ball_max = 26

        number_count = len(number_list) + 1

        valid = True

        # not a numeric value
        if not isinstance(number, int):
            valid = False

        # less than lower limit
        elif number < 1:
            valid = False

        # already has six numbers
        elif number_count > 6:
            valid = False

        # invalid white ball - either out of range or repeated.
        elif number_count < 6 and (number > white_ball_max or number in number_list):
            valid = False

        # invalid power ball - out of range
        elif number_count == 6 and number > power_ball_max:
            valid = False

        else:
            valid = True

        return valid

    def is_valid_player(self):
        """
        Check if player is valid by verifying all the attributes.
        In case when player instance is created by from_input method,
        verifiction is done by default. When player instance is created
        by calling init method by providing the attributes explicitly,
        this method verifies if the instance is valid.

        Criteria for valid instance:
        1. first name and last name should be non black and not None.
        2. exactly 6 numbers in the numbers list following the valid number criterias:
           a. all numeric.
           b. within range based on which ball - white or power ball - it is.
           c. no duplicates.

        :return (bool): True if player instance is valid. False otherwise.
        """

        valid = False

        # Either name is None
        if self.first_name is None or self.last_name is None:
            valid = False

        # Either name is blank
        elif len(self.first_name.strip()) == 0 or len(self.last_name.strip()) == 0:
            valid = False

        # not exactly 6 numbers in the list.
        elif len(self.numbers) != 6:
            valid = False

        else:
            # check if all numbers are numeric.
            for num in self.numbers:
                if not isinstance(num, int):
                    return False

            white_balls = self.numbers[:5]
            power_ball = self.numbers[5]
            distinct_wb = set(white_balls)

            # minimum and maximum from the white balls to be compared with valid range.
            min_wb, max_wb = min(white_balls), max(white_balls)

            # repeated white balls.
            if len(distinct_wb) != 5:
                valid = False

            # white ball out of range.
            elif min_wb < 1 or max_wb > 69:
                valid = False

            # power ball out of range.
            elif power_ball < 1 or power_ball > 26:
                valid = False

            else:
                valid = True

        return valid

    def __str__(self):
        """
        String representation of the player instance displaying the names and ball numbers.
        In case of invalid player, error message string is given.

        :return (str): display string describing the player.
        """

        if self.is_valid_player():
            display = "{} {} {} {} {} {} {} Powerball: {} ".format(self.first_name,
                                                                   self.last_name,
                                                                   *self.numbers)
        else:
            display = "Player object is not instancited with all valid data."

        return display
