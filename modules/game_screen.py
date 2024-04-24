from pygame import Surface
import modules.game_functions as gf
from modules.maze_logic.maze import Maze
from modules.player import Player
from modules.settings import Settings

def play_game(screen: Surface, map_: Surface, mg_settings: Settings, player: Player, curr_maze: Maze)->str:
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        if gf.check_events(player, mg_settings) == "game_over":
            return "game_over"
        gf.update_screen(mg_settings, map_, screen, player,curr_maze)
        print(player.pos)