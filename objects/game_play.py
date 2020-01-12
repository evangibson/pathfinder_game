from objects import maze_obj
from objects import player_obj


class MazeGame:
    def __init__(self, MazeMap_obj):
        """Works with a MazeMap obj with player positions already assigned"""
        self.play_map = MazeMap_obj
        self.players = dict()

        # Reset effort each run of check_move
        self.last_move_error = list()

        # Create a player object for each uid
        for id in self.play_map.player_positions:
            # Run instantiation actions
            temp_player = player_obj.MazeRunner()
            temp_player.pres_pos = self.play_map.player_positions[id][0]
            self.players.update({id: temp_player})



    def check_move(self, proposed_position):
        """Currently functional but needs fine-tuning"""
        self.last_move_error = list()


        # Edges of play area check
        if proposed_position[0] < self.play_map.dims[0] - 1 and proposed_position[1] < self.play_map.dims[1] - 1:
            pass
        else:
            # Error code 101 for high bound
            self.last_move_error.append(101)

        if proposed_position[0] >= 0 and proposed_position[1] >= 0:
            pass
        else:
            # Error code 102 for low bound
            self.last_move_error.append(102)

        # Blank value and out-of-bounds check
        # Out of bounds value will produce an index error
        if self.play_map.maze[proposed_position] == self.play_map.blank_value:
            pass
        else:
            # Error code 103 for blank value
            self.last_move_error.append(103)

        # Final check for true vs. false
        if len(self.last_move_error) == 0:
            pass_val = True
        else:
            pass_val = False

        return pass_val

    # Request action from each player
    def action_request(self, mazerunner):

        """UNSTABLE"""

        # Used for overwrite and reverting to original value in the event of a movement failure
        first_pos = mazerunner.pres_pos

        # Start by requesting move actions

        # Action acceptance check and loop for correction
        accept = False
        while accept is False:
            mazerunner.move_action(input("Move Direction: "))

            # check value at proposed position
            if self.play_map.maze[mazerunner.pres_pos] in self.play_map.blank_value:

                # Needs statement for overwriting present maze position
                accept = True

            else:
                print("ACTION FAILED. Please try again.")



def main(human_game = False):
    if human_game is True:
        # Memory saving step. Human games will not feel extra imports as heavily as ML games
        import time

        # Spacesaver for human games stepping

    else:
        print("Spacesaver")

# Still testing. No need to run yet

#if __name__ == "__main__":
#    main()
