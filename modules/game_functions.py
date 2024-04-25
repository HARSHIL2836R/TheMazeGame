'''Module for refactoring the game'''

import random
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


def check_events(player: Player, mg_settings: Settings) -> str:
    """
    Respond to keypresses and mouse events
    Args:
        None
    Returns:
        None
    """
    keymap = {pygame.K_UP: (player.width*0,player.height*-1),
            pygame.K_DOWN: (player.width*0,player.height*1),
            pygame.K_RIGHT: (player.width*1,player.height*0),
            pygame.K_LEFT: (player.width*-1,player.height*0)}

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()
        
        if not mg_settings.move_fast:
            if event.type == pygame.KEYDOWN and event.key in keymap:
                player.move(keymap[event.key][0],keymap[event.key][1])
                #print("Move:",player.move(keymap[event.key][0],keymap[event.key][1]))

    if mg_settings.move_fast:
        keys = pygame.key.get_pressed()  # Checking pressed keys
        if keys[pygame.K_UP]:
            player.move(keymap[pygame.K_UP][0],keymap[pygame.K_UP][1])
        elif keys[pygame.K_DOWN]:
            player.move(keymap[pygame.K_DOWN][0],keymap[pygame.K_DOWN][1])
        elif keys[pygame.K_RIGHT]:
            player.move(keymap[pygame.K_RIGHT][0],keymap[pygame.K_RIGHT][1])
        elif keys[pygame.K_LEFT]:
            player.move(keymap[pygame.K_LEFT][0],keymap[pygame.K_LEFT][1])
        pygame.event.pump()

    if (player.pos[0]//2+1,player.pos[1]//2+1) == mg_settings.dim:
        return "game_over"

def update_screen(mg_settings: Settings, map_: pygame.Surface, screen: pygame.Surface, player: Player, maze: Maze):
    """
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
    wall_images = mg_settings.use_walls
    path_image = mg_settings.path_image


    if mg_settings.MODE == "map":
        wall_counter = 0
        x=0
        for i in range(np.shape(maze.mazrix)[0]):
            y=0
            for j in range(np.shape(maze.mazrix)[1]):
                if maze.mazrix[j][i] == 0:
                    map_.blit(pygame.transform.scale(path_image,(width,height)),[x,y,width,height])
                if maze.mazrix[j][i] == -1:
                    map_.blit(pygame.transform.scale(wall_images[wall_counter],(width,height)),[x,y,width,height])
                    wall_counter += 1
                y+=height
            x+=width
        player.bltime()
    
    if mg_settings.MODE == "camera":
        #ADD SPRITES TO GROUP
        all_sprites = pygame.sprite.Group()

        wall_counter = 0
        #MAKE OUTER WALLS
        x=-width
        y=0
        for j in range(np.shape(maze.mazrix)[1]):
            wall_sprite = Sprite(map_,pygame.transform.scale(wall_images[wall_counter],(width,height)),width,height)
            wall_counter += 1
            wall_sprite.rect.x = x
            wall_sprite.rect.y = y
            all_sprites.add(wall_sprite)
            y+=height
        y=-height
        x=-width
        for i in range(np.shape(maze.mazrix)[0]+1):
            wall_sprite = Sprite(map_,pygame.transform.scale(wall_images[wall_counter],(width,height)),width,height)
            wall_counter += 1
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
                    wall_sprite = Sprite(map_,pygame.transform.scale(wall_images[wall_counter],(width,height)),width,height)
                    wall_counter +=1
                    wall_sprite.rect.x = x
                    wall_sprite.rect.y = y
                    all_sprites.add(wall_sprite)
                y+=height
            x+=width
        
        all_sprites.add(player)

        camera = Camera(screen, map_, mg_settings)
        camera.update(player)

        camera.draw(screen,all_sprites)

def build_maze(dim: tuple,difficulty: int,start_point: tuple,end_point: tuple):

    my_maze = Maze(dim)
    my_maze = builder.build_maze(my_maze,difficulty,start_point, end_point)
    print(my_maze.mazrix)
    print(my_maze.solution_.directions)
    return my_maze