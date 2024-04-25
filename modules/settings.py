'''Module to store the Settings class'''
from pygame import Surface
from modules.maze_logic.maze import Maze
#from maze_logic.maze import Maze
from modules.player import Player
import os.path

class Settings():
    """A class to store all settings for Maze Game"""

    def __init__(self):
        """Initialise the game's settings."""
        #Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (144,43,245)
        self.dim = (10,10)
        self.MODE = "camera"
        self.move_fast = True
        self.timeout = 15000 #milliseconds
        self.start_point = (0,0)
        self.end_point = (10,10)

    def set_dim(self, screen: Surface, maze: Maze):
        self.box_width = screen.get_width() / maze.mazrix.shape[0]
        self.box_height = screen.get_height() / maze.mazrix.shape[1]

    class Menu():
        def __init__(self) -> None:
            """Menu Settings"""
            Settings.__init__(self)
            self.screen_color = (145,63,146)
            self.screen_text_color = (255,255,255)
            self.lvl_button_width = self.screen_width/5
            self.lvl_button_height = 60
            self.active_bt_color = 	(0,0,255)
            self.inactive_bt_color = (35,58,119)
            self.bt_text_color = (255,255,255)
    
    class End():
        def __init__(self) -> None:
            """End Screen Settings"""
            Settings.__init__(self)
            self.screen_color = (0,0,0)
            self.active_bt_color = 	(0,0,255)
            self.inactive_bt_color = (35,58,119)
            self.bt_text_color = (255,255,255)

    class ScoreBoard():
        def __init__(self) -> None:
            """
            Data stored in csv file in the format: time,score,time_taken,timeout(bool)
            """
            #Load data
            f = open(os.path.dirname(__file__)+'/../data/saved_data.csv')
            self.data = []
            for line in f.readlines():
                self.data.append(line)
            f.close()
            if self.data[-1] != "\n":
                self.data.append("\n")

            #Initiate current_score
            self.curr_score = 0
        
        def add_score(self,line: str):
            self.data.append(line)

        def write_to_file(self):
            f = open(os.path.dirname(__file__)+'/../data/saved_data.csv',mode="w")
            for line in self.data:
                f.write(line)
            print("Score saved")
            f.close()

        def update_score(self,player: Player, maze: Maze, end_point: tuple):
            self.curr_score = (player.pos[0] - end_point[0])**2 + (player.pos[1] - end_point[1])**2

        def iterable_data(self)->list:
            iter_data = []
            for line in self.data:
                iter_data.append(line.split(','))
            return iter_data

if __name__ == "__main__":
    score = Settings.ScoreBoard()