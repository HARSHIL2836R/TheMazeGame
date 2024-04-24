'''Module for refactoring the game'''

import sys
import pygame
import numpy as np

#My Modules
import modules.maze_logic.builder as builder
from modules.maze_logic.maze import Maze
from modules.player import Player
from modules.settings import Settings
from modules.camera import Camera
from modules.sprites import Sprite

MODE = "camera"

def check_events(player: Player) -> None:
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
        
        keymap = {pygame.K_UP: (player.width*0,player.height*-1),
                pygame.K_DOWN: (player.width*0,player.height*1),
                pygame.K_RIGHT: (player.width*1,player.height*0),
                pygame.K_LEFT: (player.width*-1,player.height*0)}

        if event.type == pygame.KEYDOWN and event.key in keymap:
            player.move(keymap[event.key][0],keymap[event.key][1])
            #print("Move:",player.move(keymap[event.key][0],keymap[event.key][1]))

def update_screen(mg_settings: Settings, map_: pygame.Surface, screen: pygame.Surface, player: Player, maze: Maze):
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

    #DRAW THE MAZE
    width = mg_settings.box_width
    height = mg_settings.box_height
    wall_image = pygame.image.load('images/wall.jpeg')
    path_image = pygame.image.load('images/path.png')
    if MODE == "map":
        print(pygame.sprite.Group())
        x=0
        for i in range(np.shape(maze.mazrix)[0]):
            y=0
            for j in range(np.shape(maze.mazrix)[1]):
                if maze.mazrix[j][i] == 0:
                    map_.blit(pygame.transform.scale(path_image,(width,height)),[x,y,width,height])
                if maze.mazrix[j][i] == -1:
                    map_.blit(pygame.transform.scale(wall_image,(width,height)),[x,y,width,height])
                y+=height
            x+=width
        player.bltime()
    
    if MODE == "camera":
        #ADD SPRITES TO GROUP
        all_sprites = pygame.sprite.Group()

        #MAKE OUTER WALLS
        x=-width
        y=0
        for j in range(np.shape(maze.mazrix)[1]):
            wall_sprite = Sprite(map_,pygame.transform.scale(wall_image,(width,height)),width,height)
            wall_sprite.rect.x = x
            wall_sprite.rect.y = y
            all_sprites.add(wall_sprite)
            y+=height
        y=-height
        x=-width
        for i in range(np.shape(maze.mazrix)[0]+1):
            wall_sprite = Sprite(map_,pygame.transform.scale(wall_image,(width,height)),width,height)
            wall_sprite.rect.x = x
            wall_sprite.rect.y = y
            all_sprites.add(wall_sprite)
            x+=width
        #OUTER WALLS DONE

        x=0
        for i in range(np.shape(maze.mazrix)[0]):
            y=0
            for j in range(np.shape(maze.mazrix)[1]):
                if maze.mazrix[j][i] == 0:
                    path_sprite = Sprite(map_,pygame.transform.scale(path_image,(width,height)),width,height)
                    path_sprite.rect.x = x
                    path_sprite.rect.y = y
                    all_sprites.add(path_sprite)
                elif maze.mazrix[j][i] == -1:
                    wall_sprite = Sprite(map_,pygame.transform.scale(wall_image,(width,height)),width,height)
                    wall_sprite.rect.x = x
                    wall_sprite.rect.y = y
                    all_sprites.add(wall_sprite)
                y+=height
            x+=width
        
        all_sprites.add(player)

        camera = Camera(screen, map_, mg_settings)
        camera.update(player)

        camera.draw(screen,all_sprites)

    pygame.display.update()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def build_maze(dim: tuple):

    my_maze = Maze(dim)
    my_maze = builder.build_maze(my_maze,1)
    print(my_maze.mazrix)
    print(my_maze.solution_.directions)
    return my_maze