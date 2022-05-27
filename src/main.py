import argparse
import logging
from os import environ

from game import Game


def _get_arg_parser() -> argparse.ArgumentParser:
    """Build the command line parser object"""
    parser = argparse.ArgumentParser(
        prog="Mastermind",
        description="Guess the 4-digit number sequence in order to win!",
    )
    parser.add_argument(
        "-c",
        "--chances",
        type=int,
        choices=[i for i in range(1, 10)],
        default=10,
        metavar="\b",
        help="Number of guesses player will have (1-10)",
    )
    parser.add_argument(
        "-l",
        "--log-level",
        choices=["debug", "info", "warning", "error", "critical"],
        default="info",
        metavar="\b",
        help="Log level (debug|info|warning|error|critical)",
    )
    return parser


def _get_args() -> argparse.Namespace:
    """Build args namespace from parser object"""
    parser = _get_arg_parser()
    args = parser.parse_args()
    print("chances", args.chances)
    return args


def _logger_init(log_level: str):
    """Initialize logger, logger handlers and logger format"""
    formatter = logging.Formatter("%(name)s:%(levelname)s - %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger("mastermind")
    logger.addHandler(handler)
    logger.setLevel(log_level.upper())


def main():
    """Initialize the app and run the game"""
    args = _get_args()
    _logger_init(args.log_level)
    game = Game(args.chances)
    game.run()


if __name__ == "__main__":
    main()
