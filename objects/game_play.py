import maze_obj
import player_obj


class MazeGame:
    def __init__(self, MazeMap_obj):
        """Works with a MazeMap obj with player positions already assigned"""
        self.play_map = MazeMap_obj
        self.players = dict()

        # Create a player object for each uid
        for id in self.play_map.player_positions:
            # Run instantiation actions
            temp_player = player_obj.MazeRunner()
            temp_player.pres_pos = self.play_map.player_positions[id][0]
            self.players.update({id: temp_player})


    def check_move(self, nonsense_arg):
        """Currently functional but needs fine-tuning"""

        pass_val = False

        # Zero bounds check
        if nonsense_arg[0] >= 0 or nonsense_arg[1] >= 0:
            pass_val = True
        else:
            pass

        # Edges of play area check
        if nonsense_arg[0] < test_game.play_map.dims[0] - 1 or nonsense_arg[1] < test_game.play_map.dims[1] - 1:
            pass_val = True
        else:
            pass

            # Blank value check
        if test_game.play_map.maze[nonsense_arg] is test_game.play_map.blank_value:
            pass_val = True
        else:
            pass

        return pass_val

    # Request action from each player
    def action_request(self, mazerunner, maze_obj_, allow_spaces=self.maze_obj_.blank_value):

        """UNSTABLE"""

        first_pos = mazerunner.pres_pos

        # Start by requesting move actions

        # Action accepted
        accept = False
        while accept is False:
            mazerunner.move_action(input("Move Direction: "))

            # check value at proposed position
            if maze_obj_.maze[mazerunner.pres_pos] in allow_spaces:

                maze_obj.maze
                accept = True

            else:
                continue



def main(human_game = False):
    if human_game is True:
        # Memory saving step. Human games will not feel extra imports as heavily as ML games
        import time

        # Spacesaver for human games stepping

    else:
        print("Spacesaver")

if __name__ == "__main__":
    main()
