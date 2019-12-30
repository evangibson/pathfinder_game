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


def main(human_game = False):
    if human_game is True:
        # Memory saving step. Human games will not feel extra imports as heavily as ML games
        import time

        # Spacesaver for human games stepping

    else:
        print("Spacesaver")

if __name__ == "__main__":
    main()
