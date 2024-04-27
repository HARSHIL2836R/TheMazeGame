'''Module to store the Settings class which includes the general game settings, the menu settings, the end-scren settings and the Scoreboard class'''

import math
import random
import re
from pygame import Surface,image as pyimage
import os.path

#My modules
from modules.maze_logic.maze import Maze
from modules.player import Player
from modules.timer import Timer

class Settings():
    """A class to store all settings for Maze Game"""

    def __init__(self)->None:
        """Initialise the game's settings.
        The settings Initialised are:
        Screen width, Screen Height, Background Colour, Difficulty of current game, Dimensions of current Game, Game mode (camera/map), Player speed (whether on long keypress player keeps moving or not), Time given for current game, Start Point (Coordinates(x,y)), End Point, Image of the Surface of path, Images of Surface of Walls, Image of the Surface of End Point 
        """
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
        self.enable_enemies = True
        self.no_of_enemies = 1

    def set_dim(self, screen: Surface, maze: Maze)->None:
        """
        Function to set Dimensions of the Game in the attribute of Settings, dim (tuple)
        """
        self.box_width = screen.get_width() / maze.mazrix.shape[0]
        self.box_height = screen.get_height() / maze.mazrix.shape[1]

        if self.difficulty == 3:
            self.box_width *= 2
            self.box_height *= 2

    def create_wall_images_list(self, no_of_walls):
        """
        Create a list of images to iterate from when blitting the walls. Randomly add a wall from given images this list and repeat until all walls are filled.
        Args:
            no_of_walls: number of walls in the game, used to determine the length of this list
        Returns:
            None: creates an attribute of the given object, use_walls (list)
        """
        self.use_walls = []
        for i in range(no_of_walls):
            self.use_walls.append(random.choice(self.wall_images))

    class Menu():
        def __init__(self) -> None:
            """Menu Settings
            The Settings initialised are:
            Background Color, Text Color, Level Buttons width, height, Active Button color (when hovered), Inactive Button color, Button Text color
            """
            Settings.__init__(self)
            self.screen_color = (16, 24, 32)
            self.screen_text_color = (254, 231, 21)
            self.lvl_button_width = self.screen_width/6
            self.lvl_button_height = 60
            self.active_bt_color = 	(203, 0, 0)
            self.inactive_bt_color = (228, 234, 140)
            self.bt_text_color = (0,0,0)
    
    class GameScreen():
        def __init__(self) -> None:
            self.bt_color = (80, 49, 255)
            self.text_color = (228, 234, 140)
    class End():
        def __init__(self) -> None:
            """End Screen Settings
            The Settngs initialised are:
            Screen Color, Active Button color, Inactive Button color, Button Text color
            """
            Settings.__init__(self)
            self.screen_color = (0,0,60)
            self.active_bt_color = 	(0,0,255)
            self.inactive_bt_color = (35,58,119)
            self.bt_text_color = (255,255,255)

    class ScoreBoard():
        def __init__(self) -> None:
            """
            The Scoreboard object
            On initiailisation it loads data from file data/saved_data.csv into a list as a attribute of the object
            Data is stored in csv file in the format: time,score,time_taken,timeout(bool)
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
            """
            Add current game's score to the loaded data list (self.data)
            Args:
                line: str, comma separated values in the provided format (time,score,time_taken,timeout(bool))
            Returns: None
            """
            self.data.append(line)

        def write_to_file(self):
            """
            Write the data in object's attribute self.data to the file data/saved_data.csv
            """
            f = open(os.path.dirname(__file__)+'/../data/saved_data.csv',mode="w")
            for line in self.data:
                f.write(line)
            print("Score saved")
            f.close()

        def update_score(self,player: Player, maze: Maze, end_point: tuple, timer: Timer):
            """
            Update current score based on the provided information (arguments)
            Score here is essentially a weighted sum of linearly spanned exponential of fraction of distance and fraction of remaining time
            Args:
                player: Player, use position from this object
                maze: Maze
                end_point: tuple, use it's coordinates to calculate distance between it and the player
            Returns:
                None
            """
            max_dist = (end_point[0]*2)**2 + (end_point[1]*2)**2
            dist = (player.pos[0] - end_point[0]*2)**2 + (player.pos[1] - end_point[1]*2)**2
            w1 = 70 # Distance
            w2 = 30 # Time Remaining
            self.curr_score = (w1*100*(math.exp(-2*dist/max_dist)-math.exp(-2)) + w2*100*(timer.time_remaining/(timer.end_time-timer.start_time)))/(w1+w2)
            self.curr_score = "{0:.2f}".format(self.curr_score)

        def iterable_data(self)->list:
            """
            Returns loaded data as a list of list of saved values using the str.split() function
            """
            iter_data = []
            for line in self.data:
                iter_data.append(line.split(','))
            return iter_data

        def get_top_scores(self)->list:
            """
            Returns data list sorted in descending order of scores
            """
            data = self.iterable_data()
            if len(data) == 1:
                return None
            sorted_data = sorted(data[1:], key=lambda x: float(x[1]), reverse=True)
            return sorted_data

#Just for checking working of class during creating it
if __name__ == "__main__":
    score = Settings.ScoreBoard()