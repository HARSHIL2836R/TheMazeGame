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
    screen = pygame.display.set_mode((mg_settings.screen_width, mg_settings.screen_height))
    pygame.display.set_caption("The Maze Game")

    '''
    if menu.show(screen) == "exit":
        quit()
    '''
    #Intanciate the player
    player = Player(screen)

    curr_maze=gf.build_maze()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        gf.update_screen(mg_settings, screen, player,curr_maze)

run_game()