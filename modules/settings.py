'''Module to store the Settings class'''
import math
import random
from pygame import Surface,image as pyimage
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
        self.bg_color = (100,168,207)
        self.difficulty = 1
        self.dim = (10,10)
        self.MODE = "camera"
        self.move_fast = False
        self.timeout = 15000 #milliseconds
        self.start_point = (0,0)
        self.end_point = (10,10)
        self.path_image = pyimage.load('images/sky.jpg')
        self.wall_images = []
        for i in range(1,7):
            self.wall_images.append(pyimage.load('images/block'+str(i)+'.jpeg'))
        self.nest_image = pyimage.load('images/nest.png')

    def create_wall_images_list(self, no_of_walls):
        self.use_walls = []
        for i in range(no_of_walls):
            self.use_walls.append(random.choice(self.wall_images))

    def set_dim(self, screen: Surface, maze: Maze):
        self.box_width = screen.get_width() / maze.mazrix.shape[0]
        self.box_height = screen.get_height() / maze.mazrix.shape[1]

        if self.difficulty == 3:
            self.box_width *= 2
            self.box_height *= 2

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
            if self.data[-1][-2:] != "\n":
                self.data[-1] += "\n"

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
            max_dist = (end_point[0]*2)**2 + (end_point[1]*2)**2
            dist = (player.pos[0] - end_point[0]*2)**2 + (player.pos[1] - end_point[1]*2)**2
            self.curr_score = 110*(math.exp(-2*dist/max_dist)-math.exp(-2))
            if dist == 0:
                self.curr_score = 100.00
            self.curr_score = "{0:.2f}".format(self.curr_score)

        def iterable_data(self)->list:
            iter_data = []
            for line in self.data:
                iter_data.append(line.split(','))
            return iter_data

if __name__ == "__main__":
    score = Settings.ScoreBoard()