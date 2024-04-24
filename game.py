import pygame
#In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the right

#import user defined modules
from modules.settings import Settings
from modules.player import Player
import modules.game_functions as gf
import modules.menu as menu
from modules.game_screen import play_game

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    mg_settings = Settings()

    #set screen dimensions and title

    if mg_settings.MODE == "map":
        #display map_
        map_ = pygame.display.set_mode((mg_settings.screen_width,mg_settings.screen_height))
        #not needed indeed here
        screen = pygame.surface.Surface((mg_settings.screen_width, mg_settings.screen_height))
        pygame.display.set_caption("The Maze Game")
    else:
        #surface for map_ (do I need this?)
        map_ = pygame.surface.Surface((mg_settings.screen_width*2,mg_settings.screen_height*2))
        #the screen to be displayed
        screen = pygame.display.set_mode((mg_settings.screen_width, mg_settings.screen_height))
        pygame.display.set_caption("The Maze Game")

    '''
    if menu.show(screen) == "exit":
        quit()
    '''

    curr_maze=gf.build_maze(mg_settings.dim,2)
    mg_settings.set_dim(map_, curr_maze)

    #Intanciate the player
    player = Player(map_,curr_maze)
    player.set_dim(mg_settings.box_width,mg_settings.box_height)

    if play_game(screen,map_,mg_settings,player,curr_maze) == "game_over":
        print("Game completed")

run_game()