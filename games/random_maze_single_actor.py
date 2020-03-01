"""Designed to be a grid-maze with random walls and a single player"""

# Import libraries
import os
import inspect
import numpy as np

# Move to main directory
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir)
object_dir = os.path.join(parentdir, "objects")


import sys
sys.path.insert(1, object_dir)

import game_play
import maze_obj
import player_obj


# Static parameters
## Score multiplier for number of times player hits wall
wall_penalty_coef = 2

# Default value for non-match
reach_goal_match = 0

# Simple computation functions


def pth_theorem(player_position, goal_position):
    """Useful for finding the Euclidean distance between two points in a maze"""
    x_dist = abs(player_position[0] - goal_position[0])
    y_dist = abs(player_position[1] - goal_position[1])

    z = x_dist**2 + y_dist**2
    return np.sqrt(z)

# Main

def main():

    # Length of maze
    length = int(input("Enter a positive, whole number for the length of the maze: "))

    # Height of maze
    height = int(input("Enter a positive, whole number for the height of the maze: "))

    # walls/total spaces
    proportion_walls = float(input("Enter a number between 0 and 1 for the proportion of walls to blank spaces: "))

    # Maximum number of turns
    turns = int(input("Maximum number of turns: "))

    # Begin by creating a stable maze and placing one player
    g_maze = maze_obj.MazeMap([height, length])
    g_maze.random_walls(proportion_walls)
    g_maze.place_player()
    g_maze.place_goal()

    # Create a current game object using the maze generated above
    active_game = game_play.MazeGame(g_maze)

    # Function to clear console
    clear = lambda: os.system('cls')


    # Game completion indicator
    game_win = False


    for t in range(0, turns):
        # Giving feedback to the actor

        wp = wall_penalty_coef * active_game.num_errors
        dt = pth_theorem(active_game.players[next(iter(active_game.players))].pres_pos,
                         active_game.play_map.goal_position)
        score = -t - wp - dt

        # Clears console to give illusion of maze movement
        clear()

        # Use next iter because we assume only one item in player dictionary
        print("Current Turn: ", str(t))
        print("Distance to Target: ", str(dt))
        print("Penalty Score: ", str(wp))
        print("Score: ",  str(score))
        print(active_game.play_map.maze)
        active_game.action_request(active_game.players[next(iter(active_game.players))])
        print("Turns Remaining: ", str(turns - t))

        #
        final_turns = t
        if active_game.reach_goal is True:
            # Arbitrary scoring for reward
            # This variable shadowing is intentional
            reach_goal_match = 10
            break

        else:
            reach_goal_match = 0

    clear()
    print("GAME OVER")

    # This overwrites the final wp for the last bit of feedback
    wp = wall_penalty_coef * active_game.num_errors
    dt = pth_theorem(active_game.players[next(iter(active_game.players))].pres_pos,
                     active_game.play_map.goal_position)
    final_score = reach_goal_match-final_turns - wp - dt

    print("Final Score: ", str(final_score))
    print(active_game.play_map.maze)


if __name__ == "__main__":
    main()

