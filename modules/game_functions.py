'''Module storing the functions to control the player and draw out the sprites'''

import random
import sys
import pygame
import numpy as np

#My Modules
import modules.maze_logic.builder as builder
from modules.maze_logic.maze import Maze
from modules.player import Enemy, Player
from modules.settings import Settings
from modules.camera import Camera
from modules.sprites import Sprite


def check_events(player: Player, mg_settings: Settings, enemies) -> str:
    """
    Respond to keypresses and mouse events
    Args:
        player: Player
        mg_settings: Settings
    Returns:
        str, "game_over" if player reaches the end point
    """
    keymap = {pygame.K_UP: (player.width*0,player.height*-1),
            pygame.K_DOWN: (player.width*0,player.height*1),
            pygame.K_RIGHT: (player.width*1,player.height*0),
            pygame.K_LEFT: (player.width*-1,player.height*0)}

    for enemy in enemies:
        if pygame.sprite.collide_mask(enemy,player) and not enemy.die:
            enemy.die = True
            if player.lives == 1:
                return "player_died"
            else:
                player.lives -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            player.image = player.left_face
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            player.image = player.right_face

        if not mg_settings.move_fast:
            if event.type == pygame.KEYDOWN and event.key in keymap:
                if not player.move(keymap[event.key][0],keymap[event.key][1]):
                    if not mg_settings.is_muted:
                        pygame.mixer.Sound('audio/ducky-toy-sound.mp3').play()
                #print("Move:",player.move(keymap[event.key][0],keymap[event.key][1]))

    if mg_settings.move_fast:
        keys = pygame.key.get_pressed()  # Checking pressed keys
        if keys[pygame.K_UP]:
            if not player.move(keymap[pygame.K_UP][0],keymap[pygame.K_UP][1]):
                if not mg_settings.is_muted:
                    pygame.mixer.Sound('audio/duck-toy-sound.mp3').play()
        elif keys[pygame.K_DOWN]:
            if not player.move(keymap[pygame.K_DOWN][0],keymap[pygame.K_DOWN][1]):
                if not mg_settings.is_muted:
                    pygame.mixer.Sound('audio/duck-toy-sound.mp3').play()
        elif keys[pygame.K_RIGHT]:
            if not player.move(keymap[pygame.K_RIGHT][0],keymap[pygame.K_RIGHT][1]):
                if not mg_settings.is_muted:
                    pygame.mixer.Sound('audio/duck-toy-sound.mp3').play()
        elif keys[pygame.K_LEFT]:
            if not player.move(keymap[pygame.K_LEFT][0],keymap[pygame.K_LEFT][1]):
                if not mg_settings.is_muted:
                    pygame.mixer.Sound('audio/duck-toy-sound.mp3').play()
        pygame.event.pump()

    if (player.pos[0],player.pos[1]) == (mg_settings.end_point[0]*2,mg_settings.end_point[1]*2):
        return "game_over"

def update_screen(mg_settings: Settings, map_: pygame.Surface, screen: pygame.Surface, player: Player, maze: Maze, enemies: list[Enemy]):
    """
    Args:
        mg_settings: Settings, the settings class containing all game settings
        map_: Surface, the surface over which all Sprite rectangles lie
        screen: Surface, the screen used for display of the running game
        player: Player, the player class used to control all player events
        maze: Maze, the Maze object over which current game runs
    Returns:
        None
    """
    #Redraw the screen during each pass through the loop
    screen.fill(mg_settings.bg_color)

    #DRAW THE MAZE
    width = mg_settings.box_width
    height = mg_settings.box_height
    wall_images = mg_settings.use_walls
    path_image = mg_settings.path_image
    nest_image = mg_settings.nest_image

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

        #Draw Nest
        nest_sprite = Sprite(map_,pygame.transform.scale(nest_image,(width,height)),width,height)
        nest_sprite.rect.x = mg_settings.end_point[0]*2*width
        nest_sprite.rect.y = mg_settings.end_point[1]*2*height
        all_sprites.add(nest_sprite)

        all_sprites.add(player)
        for enemy in enemies:
            if not enemy.die:
                all_sprites.add(enemy)

        camera = Camera(screen, map_, mg_settings)
        camera.update(player)

        camera.draw(screen,all_sprites)

def build_maze(dim: tuple,difficulty: int,start_point: tuple,end_point: tuple)->Maze:
    """
    Simple function to build maze given dimensions,difficulty and start and stop points
    """
    my_maze = Maze(dim)
    my_maze = builder.build_maze(my_maze,difficulty,start_point, end_point)
    print(my_maze.mazrix)
    np.savetxt('last_maze.txt',my_maze.mazrix,fmt="%3d")
    print(my_maze.solution_.directions)
    print(my_maze.solution_.walk)
    return my_maze