'''Module for customising the Menu'''
import pygame
from modules.button import Button

def show(screen: pygame.Surface):
    """
    Displays the menu on the screen
    Args:
        screen: Surface, the screen used to display menu
    Returns:
        None
    """
    #white color
    color = (255,255,255)
    # light shade of the button  
    color_light = (170,170,170)
    # dark shade of the button  
    color_dark = (100,100,100)
    
    screen.fill(color)
    
    menu_surface = screen.subsurface(screen.get_rect().center, (screen.get_width()/2, screen.get_height()/3))
    play_button = Button(menu_surface, "Play", color_light, color_dark, 200, 60, screen.get_rect().center)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        play_button.draw_button()
        #Keep Updating the Screen
        pygame.display.update()