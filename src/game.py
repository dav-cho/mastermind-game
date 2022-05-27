import logging
import sys
from collections import OrderedDict
from typing import Tuple

import requests

from prompt import Prompt

BASE_URL = "https://www.random.org/integers/"


class Game:
    """
    Attributes:
      self.lives:       Number of chances to guess correctly.
      self.num_digits:  Number of digits in the randomly generated number combination.
      self.num_range:   (0-9) Range of numbers to include in the number combination.
      self.logger:      Name of the logger.

      self.numbers:  The correct numbers to guess generated from random.org's API.
      self.prompt:   Text outputs from the Prompt class.
      self.guesses:  Set containing history of player guesses.
    """

    def __init__(
        self,
        lives: int = 10,
        num_digits: int = 4,
        num_range: Tuple[int, int] = (1, 8),
        logger: str = "mastermind",
    ):
        self.lives = lives
        self.num_digits = num_digits
        self.num_range = num_range
        self.logger = logging.getLogger(logger)
        self.numbers: str = ""
        self.guesses: OrderedDict[str, int] = OrderedDict()
        self.last_result: str = ""
        self.prompt = Prompt()
        self.guesses_remaining = lambda: self.lives - len(self.guesses)

    def run(self):
        """Run an instance of the game"""
        self.prompt.intro()

        ready = self.check_start()
        if not ready:
            self.prompt.goodbye()
            sys.exit()

        self.start()
        win = False
        while not win and self.guesses_remaining():
            guess = self.player_guess()
            win = self.check_win(guess)

        if win:
            self.prompt.you_win(self.numbers)
        else:
            self.prompt.out_of_guesses()
            self.prompt.you_lose()

        play_again = self.play_again()
        if play_again:
            game = Game(self.lives)
            game.run()
        else:
            self.prompt.goodbye()

    def check_start(self) -> bool:
        """Prompt player to begin game"""
        valid_choices = ("yes", "no")
        ready = ""
        while ready not in valid_choices:
            ready = input(self.prompt.PLAYER_READY).lower()
        return True if ready == "yes" else False

    def start(self):
        """Simulate that the computer is thinking while generating random numbers"""
        self.prompt.start()
        self.numbers = self.get_random_numbers(self.num_digits, *self.num_range)

    def player_guess(self) -> str:
        """Take player input for each guess and validate proper input format."""
        guess = ""
        while not self.valid_player_guess(guess):
            self.prompt.history(
                self.guesses, self.last_result, self.guesses_remaining()
            )
            self.logger.debug(f"Winning Numbers: {self.numbers}\n")
            guess = input(self.prompt.PLAYER_GUESS)
        score = self.get_score(guess)
        self.guesses[guess] = score
        self.last_result = self.prompt.GUESS_RESULT[score]
        return guess

    def check_win(self, guess: str) -> bool:
        if guess == self.numbers:
            return True
        return False

    def play_again(self) -> bool:
        valid_choices = ("yes", "no")
        choice = ""
        while choice not in valid_choices:
            choice = input(self.prompt.PLAY_AGAIN).lower()
        if choice == "yes":
            return True
        return False

    def get_random_numbers(
        self, num: int, min: int, max: int, col=4, base=10, format="plain", rnd="new"
    ) -> str:
        """
        Generate 4 random numbers using the random.org API

        Paramaters:
            num:    The number of integers requested.
            min:    The smallest value allowed for each integer.
            max:    The largest value allowed for each integer.
            col:    The number of columns in which the integers will be arranged.
                    (For the purposes of this app, it is best to set this equal to
                    the 'num' parameter.)
            base:   2 | 8 | 10 | 16
            format: html | plain
            rnd:    new | id.identifier | date.iso-date

        Documentation: https://www.random.org/clients/http/api/
        """
        query_params = (
            f"num={num}",
            f"min={min}",
            f"max={max}",
            f"col={col}",
            f"base={base}",
            f"format={format}",
            f"rnd={rnd}",
        )
        url = f"{BASE_URL}?{'&'.join(query_params)}"
        response = requests.get(url)
        self.logger.debug(f"Response status: {response.status_code}")
        if not response.ok:
            self.logger.error(f"Request Error! Response Status: {response.status_code}")
            sys.exit()
        return response.text.replace("\t", "").strip()

    def valid_player_guess(self, guess) -> bool:
        if guess in self.guesses:
            self.last_result = self.prompt.ALREADY_GUESSED
            return False
        valid_length = len(guess) == self.num_digits
        valid_digits = all([char.isdigit() for char in guess])
        return valid_length and valid_digits

    def get_score(self, guess: str) -> int:
        correct_digit = False
        correct_position = False
        for i, digit in enumerate(guess):
            if digit in self.numbers:
                correct_digit = True
            if digit == self.numbers[i]:
                correct_position = True
                break
        score = correct_digit + correct_position
        return score
