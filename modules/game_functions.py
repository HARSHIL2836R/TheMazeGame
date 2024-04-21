'''Module for refactoring the game'''

import sys
import pygame
import numpy as np

#My Modules
import modules.maze_logic.builder as builder
from modules.maze_logic.maze import Maze
from modules.settings import Settings

def check_events() -> None:
    """
    Respond to keypresses and mouse events
    Args:
        None
    Returns:
        None
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

def update_screen(mg_settings: Settings, screen: pygame.Surface, player, maze: Maze):
    """
    Update images on screen and flip to the new screen
    Args:
        mg_settings: Settings, the settings class containing all game settings
        screen: Surface, the screen used for display of the running game
        player: Player, the player class used to control all player events
    Returns:
        None
    """
    #Redraw the screen during each pass through the loop
    screen.fill(mg_settings.bg_color)
    #old code: player.bltime()

    width = screen.get_width()/np.shape(maze.mazrix)[0]
    height = screen.get_height()/np.shape(maze.mazrix)[1]
    x=0
    for i in range(np.shape(maze.mazrix)[0]):
        y=0
        for j in range(np.shape(maze.mazrix)[1]):
            if maze.mazrix[j][i] == 0:
                pygame.draw.rect(screen,'white',[x,y,width,height])
            y+=height
        x+=width
    
    pygame.display.update()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def build_maze():

    my_maze = Maze((10,10))
    my_maze = builder.build_maze(my_maze,1)
    print(my_maze)
    return my_maze