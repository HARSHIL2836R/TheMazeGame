import pygame
#In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the right

#import user defined modules
from modules.settings import Settings
from modules.player import Player
import modules.game_functions as gf
import modules.menu as menu

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    mg_settings = Settings()

    #set screen dimensions and title

    #surface for map_ (do I need this?)
    map_ = pygame.surface.Surface((mg_settings.screen_width*2,mg_settings.screen_height*2))
    #the screen to be displayed
    screen = pygame.display.set_mode((mg_settings.screen_width, mg_settings.screen_height))
    pygame.display.set_caption("The Maze Game")

    '''
    if menu.show(screen) == "exit":
        quit()
    '''

    curr_maze=gf.build_maze((10,10))
    mg_settings.set_dim(map_, curr_maze)

    #Intanciate the player
    player = Player(map_,curr_maze)
    player.set_dim(mg_settings.box_width,mg_settings.box_height)

    print(curr_maze.solution_.directions)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(player)
        gf.update_screen(mg_settings, map_, screen, player,curr_maze)

run_game()