# Python Mastermind Game

A CLI number guessing game written in Python.

**Dependency List**

| Dependency             | Link                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| Python 3.10.x          | [python.org](https://www.python.org/downloads/)                                              |
| Pipenv                 | [pipenv.pypa.io](https://pipenv.pypa.io/en/latest/#install-pipenv-today)                     |
| Python Requests Module | [requests.readthedocs.io/en/latest](https://requests.readthedocs.io/en/latest/user/install/) |

## Instructions

You are playing against the computer which thinks it can outsmart you.  
The computer will generate a random number sequence comprised of 4 digits ranging from 1-8 inclusive.  
In order to win, you will have to guess the correct number sequence in 10 tries or less!

## Installation

### Repository

You will first need to clone this repository, or download it as a zip file by clicking the green `Code` button on the top right of [this repository's home page]()

### Python 3

In order to run this game, you will need a version of Python 3.10.

You can check if you have python installed by running the command:

`which python`

If your response says something like `python not found`, you can go to the official [python.org](https://www.python.org/downloads/) website to download and install the latest version of Python

If you already have Python installed, you can check which version you have by running the command:

`python --version`

### Dependencies

After you have ensured your Python installation and version, you will have to install the dependencies for this app as specified in the `requirements.txt` or if using Pipenv, `Pipfile`.

You can install these dependencies globally to your Python installation, or if you are familiar with Python, you can set up a virtual environment and install the dependencies locally.

Make sure you are in the root level of your local/cloned copy of this repository.

To install it globally to your Python installation you can run:

`pip install -r requirements.txt`

If you are using Pipenv, you can install the dependencies and setup a virtual environment by running the command:

`pipenv install`

## Usage

Again make sure you are in the root level of your local/cloned copy of this repository.

If you have the `requests` module globally installed, simply run:

`python src/main.py`

With a virtual environment, you must first activate the environment. For Pipenv this command is:

`pipenv shell`

Then run:

`python src/main.py`

With Pipenv you can run the file in a previously created virtual environment without explicitly spawning the virtual environment's shell by running the following command:

`pipenv run python src/main.py`

### Options

You can run this file with several command line flags. See all the options by running:

`python src/main.py -h`

Sample Output:

```
usage: Mastermind [-h] [-l] [-c]

Guess the 4-digit number sequence in order to win!

options:
  -h, --help           show this help message and exit
  -c, --chances        Number of guesses player will have (1-10)
  -l, --log-level      Log level (debug|info|warning|error|critical)
```

- By specifying the `-c, --chances` flag, you can set the number of tries/guesses you will have before you lose.
- By setting `-l, --log-level` to `debug`, the app will log the status code from the random.org API as well as the winning numbers for debugging purposes.
