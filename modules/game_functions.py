'''Module for refactoring the game'''

import sys
import pygame

def check_events() -> None:
    """
    Respond to keypresses and mouse events
    Args:
        None
    Returns:
        None
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(mg_settings, screen, player):
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
    player.bltime()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()