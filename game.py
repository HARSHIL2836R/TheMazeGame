import numpy as np
import pygame
#In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the right

#import user defined modules
from modules.settings import Settings
from modules.player import Player
import modules.game_functions as gf
import modules.menu as menu
from modules.game_screen import play_game
import modules.end_screen as the_end

def set_display(mg_settings: Settings):
    #DISPLAY THE COMPLETE MAP
    if mg_settings.MODE == "map":
        #display map_
        map_ = pygame.display.set_mode((mg_settings.screen_width,mg_settings.screen_height))
        #not needed indeed here
        screen = pygame.surface.Surface((mg_settings.screen_width, mg_settings.screen_height))
        pygame.display.set_caption("The Maze Game")
            
    #DISPLAY HALF OF MAP
    else:
        #surface for map_ (do I need this?)
        map_ = pygame.surface.Surface((mg_settings.screen_width*2,mg_settings.screen_height*2))
        #the screen to be displayed
        screen = pygame.display.set_mode((mg_settings.screen_width, mg_settings.screen_height))
        pygame.display.set_caption("The Maze Game")
    return map_,screen    
    
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    mg_settings = Settings()

    #set screen dimensions and title
    map_,screen = set_display(mg_settings)
    if mg_settings.MODE == "map":
        menu_out = menu.show(map_)
    else:
        menu_out = menu.show(screen)

    if menu_out == "exit":
        quit()
    difficulty = menu_out
    difficulty = int(difficulty)

    #Set dimensions based on difficulty
    if difficulty == 1:
        mg_settings.dim =(5,5)
    if difficulty == 2:
        mg_settings.dim =(10,10)
    if difficulty == 3:
        mg_settings.dim = (20,20)

    pygame.display.quit()

    #BUILD MAZE
    print("Building Maze...")
    curr_maze=gf.build_maze(mg_settings.dim,int(difficulty))
    print("white",np.sum(np.where(curr_maze.mazrix == 0)))
    
    print("Building done")
    map_,screen = set_display(mg_settings)
    
    #write solution in file
    file = open('path.txt','w')
    for i in range(len(curr_maze.solution_.directions)):
        file.write(curr_maze.solution_.directions[i])
    file.close()
    mg_settings.set_dim(map_, curr_maze)

    #Intanciate the player
    player = Player(map_,curr_maze)
    player.set_dim(mg_settings.box_width,mg_settings.box_height)

    if play_game(screen,map_,mg_settings,player,curr_maze) == "game_over":
        print("Game completed")
        pygame.display.quit()

        map_,screen = set_display(mg_settings)
        print(the_end.show(screen))

def check_endscreen():
    pygame.init()
    mg_settings = Settings()
    map_,screen = set_display(mg_settings)
    if mg_settings.MODE == "map":
        the_end.show(map_)

run_game()
#check_endscreen()