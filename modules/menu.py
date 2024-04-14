'''Module for customising the Menu'''
import pygame
import sys
from modules.button import Button

def show(screen: pygame.Surface):
    """
    Displays the menu on the screen
    Args:
        screen: Surface, the screen used to display menu
    Returns:
        None
    """
    # light shade of the button  
    color_light = (170,170,170)
    # dark shade of the button  
    color_dark = (100,100,100)
    
    screen.fill('red')
    
    swidth, sheight = screen.get_rect().width,screen.get_rect().height
    
    #CREATE AND CONFIGURE BUTTONS
    lvl1_button = Button(screen, "1", color_light, color_dark, 'black', swidth/5, 60, (screen.get_rect().centerx*2/3, screen.get_rect().centery*4/6))
    lvl2_button = Button(screen, "2", color_light, color_dark,'black', swidth/5, 60, (screen.get_rect().centerx, screen.get_rect().centery*4/6))
    lvl3_button = Button(screen, "3", color_light, color_dark,'black', swidth/5, 60, (screen.get_rect().centerx*4/3, screen.get_rect().centery*4/6))
    #
    
    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        for button in {lvl1_button,lvl2_button,lvl3_button}:
            button.draw_button()
            button.update_button(mouse[0], mouse[1])
            
        #Keep Updating the Screen
        pygame.display.update()