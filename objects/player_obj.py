import numpy as np
from objects import maze_obj


class MazeRunner:
    """Builds a player for navigation through the maze"""

    def __init__(self, human=False):
        # Unique id for player
        self.id = None

        # Player present position
        self.pres_pos = list([None, None])

        # Default speed value
        self.curr_speed = 1

        # Stores maze wall value

        # Dictionary for movement schema
        self.moves = dict({"l": lambda a: [a[0], a[1] - self.curr_speed],
                           "r": lambda a: [a[0], a[1] + self.curr_speed],
                           "d": lambda a: [a[0] + self.curr_speed, a[1]],
                           "u": lambda a: [a[0] - self.curr_speed, a[1]],
                           "ul": lambda a: [a[0] - self.curr_speed, a[1] - self.curr_speed],
                           "ur": lambda a: [a[0] - self.curr_speed, a[1] + self.curr_speed],
                           "dl": lambda a: [a[0] + self.curr_speed, a[1] - self.curr_speed],
                           "dr": lambda a: [a[0] + self.curr_speed, a[1] + self.curr_speed]})

    def move_action(self, move_direction, speed=1):
        """move_direction executes relative position change:
        on a grid, (l,r,d,u) will move the MazeRunner left, right, down, or up,
        respectively.

        Using the same grid, (ur, ul, dl, dr) will move the MazeRunner up and right,
        up and left, down and left, and down and right, respectively.

        The number of spaces moved is determined by speed."""

        self.curr_speed = speed

        # Contingency for bad input
        valid_dir = False
        while valid_dir is False:
            try:
                self.pres_pos = self.moves[move_direction](self.pres_pos)
                valid_dir = True

            except IndexError:
                move_direction = input("Move direction invalid! Please try again: ")
                valid_dir = False

        return self.pres_pos
