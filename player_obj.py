import numpy as np


class MazeRunner:
    """Builds a player for navigation through the maize"""
    def __init__(self, human = False):
        if human is True:
            print("You'll probably win")
        else:
            print("Good luck robo-friend, I believe in you!")
