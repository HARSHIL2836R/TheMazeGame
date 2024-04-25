'''Module for refactoring the game'''

import sys
import time
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

def update_screen(mg_settings: Settings, map_: pygame.Surface, screen: pygame.Surface, player: Player, maze: Maze, clock: pygame.time.Clock):
    """
    Update images on screen and flip to the new screen
    Args:
        mg_settings: Settings, the settings class containing all game settings
        screen: Surface, the screen used for display of the running game
        player: Player, the player class used to control all player events
    Returns:
        None
    """
    #milliseconds
    start_ticks = clock.get_time()

    #Redraw the screen during each pass through the loop
    screen.fill(mg_settings.bg_color)
    #old code: player.bltime()

    #DRAW THE MAZE
    width = mg_settings.box_width
    height = mg_settings.box_height
    wall_image = pygame.image.load('images/wall.jpeg')
    path_image = pygame.image.load('images/path.png')

    if mg_settings.MODE == "map":
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
    
    if mg_settings.MODE == "camera":
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

        #Blit Counter
        timer = pygame.font.SysFont('Monospace',32).render(str(clock.get_time()-start_ticks),True,'white')
        screen.blit(timer,screen.get_rect().topleft)

    pygame.display.update()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def build_maze(dim: tuple,difficulty: int):

    my_maze = Maze(dim)
    my_maze = builder.build_maze(my_maze,difficulty)
    print(my_maze.mazrix)
    print(my_maze.solution_.directions)
    return my_maze