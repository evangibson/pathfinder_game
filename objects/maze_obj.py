import numpy as np
import sys
from random import randint


class MazeMap:
    """A Class that establishes a maze's environment"""

    def __init__(self,
                 dimensions,
                 wall=-1,
                 blank=0,
                 goal=-2):
        # Tuple argument for the length and width of the maze
        self.dims = dimensions

        # By default, maze will generate as blank
        self.maze = np.zeros(self.dims, dtype=int)

        # Declare wall, blank space, and goal values
        self.wall_value = wall
        self.blank_value = blank
        self.goal_value = goal

        # Storage for the wall indices
        self.wall_indices = None

        # RESERVED non-uid values. Will help from confusing uids with other value types. Designed to be added to
        self.black_list = list([self.wall_value, self.blank_value])

        # Default uid (meant to be iterated sequentially)
        self.next_play_id = 101

        # Indices that players can't be placed in
        self.forbid_indices = list()

        self.player_positions = dict()

        # Null until instantiated by place_goal
        self.goal_position = None

    def random_walls(self, prop_of_walls):
        """Builds walls within a maze based on randomization parameters"""

        # Map random indices for wall placement
        self.wall_indices = np.random.choice(np.arange(self.maze.size),
                                             replace=False,
                                             size=int(self.maze.size * prop_of_walls))

        # Add walls to forbidden zones
        self.forbid_indices.append(list(self.wall_indices))

        # Create flattened array to map
        temp_arr = self.maze.flatten()

        # Remake original structure
        temp_arr[self.wall_indices] = self.wall_value

        # Remake original structure
        self.maze = temp_arr.reshape(self.dims)

        return self.maze

    def place_player(self, start_position=None, uid=None):
        """Will randomly select a player starting position and uid if both arguments are None.
        PLEASE NOTE: Does not actually assign a MazeRunner object to a position. It merely assigns a UID and start point"""
        if start_position is None:
            temp_player_index = np.random.choice(np.arange(self.maze.size),
                                                 replace=False,
                                                 size=1)
            # Create flattened array to map
            temp_arr = self.maze.flatten()

            # Provide stop placeholder for loop
            loop_brake = 0

            while int(temp_player_index) in self.forbid_indices[0]:
                # Propose index for player to occupy
                temp_player_index = np.random.choice(np.arange(self.maze.size),
                                                     replace=False,
                                                     size=1)

                # To keep the placeholder loop from running to infinity
                loop_brake += 1
                if loop_brake > len(temp_arr):
                    sys.exit("Player Placement Failed! No unreserved space detected")
                else:
                    continue

            if uid is None:
                # Remake original structure
                temp_arr[temp_player_index] = self.next_play_id

                # Carry progress to values list
                self.black_list.append(self.next_play_id)

            elif uid not in self.black_list:
                temp_arr[temp_player_index] = uid

                # Carry progress to values list
                self.black_list.append(uid)

            else:
                sys.exit("Player Placement Failed! Proposed UID already in black_list")

            self.forbid_indices[0].append(int(temp_player_index))

            # Remake original structure
            self.maze = temp_arr.reshape(self.dims)

        if uid is None:
            self.find_player(self.next_play_id)
            self.next_play_id += 1
        else:
            self.find_player(uid)

    def find_player(self, uid, silent = True):
        """Can function to find multi-id coordinates, too"""
        full_loc_list = list()

        for i in range(0, len(np.where(self.maze == uid)[0])):
            player_loc = list([np.where(self.maze == uid)[0][i], np.where(self.maze == uid)[1][i]])
            full_loc_list.append(player_loc)

        self.player_positions.update({uid: full_loc_list})

        if silent is False:
            return dict({uid: full_loc_list})

    def place_goal(self, point = "random"):
        """If point != "random", argument MUST be a coordinate tuple"""
        if point != "random":
            self.maze[point[0]][point[1]] = self.goal_value
            self.goal_position = tuple([point[0],point[1]])

        else:
            # Find blank spaces for goal placement
            curr_blanks = np.where(self.maze == self.blank_value)

            # In a 2d array, curr_blanks should produce two arrays of equal length
            # Call one value in the range of those arrays to index
            value = randint(0, len(curr_blanks[0])-1)

            self.maze[curr_blanks[0][value]][curr_blanks[1][value]] = self.goal_value
            self.goal_position = tuple([curr_blanks[0][value],curr_blanks[1][value]])

