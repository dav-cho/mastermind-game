import logging
from dataclasses import dataclass
from time import sleep
from typing import Tuple


@dataclass
class Prompt:
    """A collection of text and methods to be displayed to stdout"""

    GREETING: str = """
               +-----------------------------------------+
               |     Welcome to the Mastermind Game!     |
               +-----------------------------------------+
    """
    INSTRUCTIONS: str = """
        You are battling against the computer in a game of wits.
        
        The computer thinks it is sneaky and has
        thought of a random 4-digit number combination.
        
        The number combination is made up of digits
        ranging from 1 to 8 inclusive.
        
        Prove that you are smarter than the computer by
        correctly guessing the number combination in 10 tries or less!

      ------------------------------------------------------------------
    """
    PLAYER_READY: str = "Are you ready to begin? Type 'Yes' or 'No': "
    COMPUTER_THINKING: Tuple[str, str, str, str] = (
        "The Computer is thinking of a hard number combination...",
        "Just a moment. The Computer is still thinking.",
        "Still thinking.....",
        "Almost there...",
    )
    COMPUTER_READY: str = (
        "Ok! The computer has some random number combination in mind..."
    )
    YOUR_TURN: str = "Now it's your turn to guess!"
    PLAYER_GUESS: str = "Enter your 4-digit guess: "
    ALREADY_GUESSED: str = "You already guessed that number."
    OUT_OF_GUESSES: str = "Sorry, you have no guesses remaining..."
    YOU_WIN: str = "You Win!!!"
    YOU_LOSE: str = "You Lost! :("
    GUESS_RESULT: Tuple[str, str, str] = (
        "Sorry, you guessed no correct digits or their positions.",
        "Nice! You guessed a correct digit!",
        "Wow! You guessed a correct digit and position!",
    )
    HISTORY_TITLE: str = """
    Guess History:
    --------------------------------"""
    HISTORY_SCORE: Tuple[str, str, str] = (
        "Completely Wrong",
        "Correct Digit",
        "Correct Digit and Position",
    )

    CLEAR = "\n" * 100
    PLAY_AGAIN = "Would you like to play again? Type 'Yes' or 'No': "
    GOODBYE = "" * 4 + "Goodbye!"

    def clear(self):
        print("\n" * 100)

    def intro(self):
        self.clear()
        print(self.GREETING)
        print(self.INSTRUCTIONS)
        self._pad(4)

    def start(self):
        self.clear()
        self._set_interval(self.COMPUTER_THINKING, 1.5)
        print(self.COMPUTER_READY)
        self._pad(1)
        print(self.YOUR_TURN)
        self._pad(3)
        sleep(1)

    def history(self, guesses, last_result, guesses_remaining):
        if guesses:
            self.clear()
            print(self.HISTORY_TITLE)
            for guess in guesses:
                score = guesses[guess]
                print(f"{guess}: {self.HISTORY_SCORE[score]}")
            self._pad(4)
        print(last_result)
        self._pad(1)

        print(f"Guesses Remaining: {guesses_remaining}")
        self._pad(1)

    def out_of_guesses(self):
        self.clear()
        print(self.OUT_OF_GUESSES)
        self._pad(2)

    def you_win(self, winning_numbers):
        self.clear()
        print(f"{winning_numbers} is correct!")
        self._pad(1)
        print(self.YOU_WIN)
        self._pad(2)

    def you_lose(self):
        print(self.YOU_LOSE)
        self._pad(2)

    def goodbye(self):
        self._pad(100)
        print(self.GOODBYE)
        self._pad(1)

    def _pad(self, num_lines):
        logger = logging.getLogger("mastermind")
        if num_lines < 0:
            logger.warning(f"num_lines must be > 0")
            return
        print("\n" * (num_lines - 1))

    def _set_interval(self, prompts: tuple, interval: float = 1):
        for i in range(len(prompts)):
            self.clear()
            print(prompts[i])
            self._pad(4)
            sleep(interval)
        self.clear()
