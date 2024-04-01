'''Module for refactoring the game'''

import sys
import pygame

def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(mg_settings, screen, player):
    """Update images on screen and flip to the new screen"""
    #Redraw the screen during each pass through the loop
    screen.fill(mg_settings.bg_color)
    player.bltime()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()