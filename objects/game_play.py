
try:
    import maze_obj
    import player_obj

except:
    from objects import maze_obj
    from objects import player_obj


class MazeGame:
    def __init__(self, MazeMap_obj):
        """Works with a MazeMap obj with player positions already assigned"""
        self.play_map = MazeMap_obj
        self.players = dict()

        # Reset effort each run of check_move
        self.last_move_error = list()

        # Number of errors in iteration
        self.num_errors = 0

        # Indicator for reaching goal
        self.reach_goal = False

        # Create a player object for each uid
        for id in self.play_map.player_positions:
            # Run instantiation actions
            temp_player = player_obj.MazeRunner()
            temp_player.pres_pos = self.play_map.player_positions[id][0]
            temp_player.id = id
            self.players.update({id: temp_player})



    def check_move(self, proposed_position):
        """Currently functional but needs fine-tuning"""
        self.last_move_error = list()


        # Edges of play area check
        if proposed_position[0] < self.play_map.dims[0] and proposed_position[1] < self.play_map.dims[1]:
            pass
        else:
            # Error code 101 for high bound
            self.last_move_error.append("e101")

        if proposed_position[0] >= 0 and proposed_position[1] >= 0:
            pass
        else:
            # Error code 102 for low bound
            self.last_move_error.append("e102")

        # Blank value and goal check
        # Out of bounds value will produce an index error
        try:
            if self.play_map.maze[proposed_position[0], proposed_position[1]] in [self.play_map.blank_value, self.play_map.goal_value]:
                pass
            else:
                # Error code 103 for blank value
                self.last_move_error.append("e103")

        except (ValueError, IndexError) as e:
            pass

        # Win check. Doesn't throw error for failure to pass

        try:
            if self.play_map.maze[proposed_position[0], proposed_position[1]] == self.play_map.goal_value:
                self.reach_goal = True
            else:
                pass
        except(IndexError):
            # We don't need to append an additional error because this behavior will already be caught by e101
            pass

        # Final check for true vs. false
        if len(self.last_move_error) == 0:
            pass_val = True
        else:
            pass_val = False

        return pass_val

    # Request action from each player
    def action_request(self, mazerunner):

        """Initiating action for a player's move. Loop will run until a valid input (true)
        is generated by checking the move against the action"""

        # Used for overwrite and reverting to original value in the event of a movement failure
        first_pos = mazerunner.pres_pos

        # Start by requesting move actions

        # Action acceptance check and loop for correction
        accept = False
        while accept is False:
            action = mazerunner.move_action(input("Move Direction: "))
            accept = self.check_move(action)

            if accept is False:
                self.num_errors += 1
                print("Move rejected")
                mazerunner.pres_pos = first_pos

        # Overwrite old position with blank value
        self.play_map.maze[first_pos[0], first_pos[1]] = self.play_map.blank_value

        # update map with player's new position
        self.play_map.maze[mazerunner.pres_pos[0], mazerunner.pres_pos[1]] = mazerunner.id

        # Update map's player position
        self.play_map.player_positions[mazerunner.id] = self.players[mazerunner.id].pres_pos
