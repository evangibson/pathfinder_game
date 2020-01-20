"""Designed to be a grid-maze with random walls and a single player"""

# Import libraries

from objects import game_play
from objects import maze_obj
from objects import player_obj

# Static parameters


# Create starting input parameters

def main():

    # Length of maze
    length = int(input("Enter a positive, whole number for the length of the maze: "))

    # Height of maze
    height = int(input("Enter a positive, whole number for the height of the maze: "))

    # walls/total spaces
    proportion_walls = float(input("Enter a number between 0 and 1 for the proportion of walls to blank spaces: "))

    # Maximum number of turns
    turns = input("Maximum number of turns: ")


    # Begin by creating a stable maze and placing one player
    g_maze = maze_obj.MazeMap([height, length])
    g_maze.random_walls(proportion_walls)
    g_maze.place_player()

    # Create a current game object using the maze generated above
    active_game = game_play.MazeGame(g_maze)

    for t in range(0, turns):
        # Giving feedback to the actor
        #print("Turn {}".format(t), end="\r"))
        #print(active_game.play_map.maze, end="\r")

        # Use next iter because we assume only one item in player dictionary
        test_game.action_request(active_game.players[next(iter(active_game.players))])

    print("GAME OVER")
    print(active_game.play_map.maze)

if __name__ == "__main__":
    main()

