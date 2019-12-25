import numpy as np

class MazeMap:
    """A Class that establishes a maze's environment"""

    def __init__(self,
                 dimensions,
                 wall = -1,
                 blank = 0):
        # Tuple argument for the length and width of the maze
        self.size = dimensions

        # By default, maze will generate as blank
        self.maze = np.zeros(self.size, dtype=int)

        # Declare wall and blank space values
        self.wall_value = wall
        self.blank_value = blank



    def random_walls(self, prop_of_walls):
        """Builds walls within a maze based on randomization parameters"""

        # Map random indices for wall placement
        indices = np.random.choice(np.arange(self.maze.size),
                                   replace=False,
                                   size=int(self.maze.size * prop_of_walls))
        # Create flattened array to map
        temp_arr = self.maze.flatten()

        # Remake original structure
        temp_arr[indices] = self.wall_value

        # Remake original structure
        self.maze = temp_arr.reshape(self.size)

        return self.maze