'''Module for customising the Menu'''
import pygame
from modules.button import Button
from modules.settings import Settings

def show(screen: pygame.Surface):
    """
    Displays the menu on the screen
    Args:
        screen: Surface, the screen used to display menu
    Returns:
        None
    """

    mg_settings = Settings.Menu()
    screen.fill(mg_settings.screen_color)
    
    #CREATE AND CONFIGURE BUTTONS
    lvl1_button = Button(screen, "1", mg_settings.active_bt_color, mg_settings.inactive_bt_color, mg_settings.bt_text_color, mg_settings.lvl_button_width, mg_settings.lvl_button_height, (screen.get_rect().centerx*2/3, screen.get_rect().height*4/6))
    lvl2_button = Button(screen, "2", mg_settings.active_bt_color, mg_settings.inactive_bt_color,mg_settings.bt_text_color, mg_settings.lvl_button_width, mg_settings.lvl_button_height, (screen.get_rect().centerx, screen.get_rect().height*4/6))
    lvl3_button = Button(screen, "3", mg_settings.active_bt_color, mg_settings.inactive_bt_color,mg_settings.bt_text_color, mg_settings.lvl_button_width, mg_settings.lvl_button_height, (screen.get_rect().centerx*4/3, screen.get_rect().height*4/6))
    #
    
    font = pygame.font.SysFont("Monospace", 70)
    title = font.render("THE MAZE GAME", True, mg_settings.screen_text_color, mg_settings.screen_color)
    font = pygame.font.SysFont("Monospace", 32)
    selector = font.render("###|Select Level|###", True, mg_settings.screen_text_color, mg_settings.screen_color)
    to_quit = font.render("Press ESC to QUIT", True, mg_settings.screen_text_color, mg_settings.screen_color)

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return "exit"

        for button in {lvl1_button,lvl2_button,lvl3_button}:
            button.draw_button()
            button.update_button(mouse[0], mouse[1])

        screen.blit(title, (screen.get_rect().centerx-title.get_rect().width/2,screen.get_rect().height*2/6))
        screen.blit(selector, (screen.get_rect().centerx-selector.get_rect().width/2,screen.get_rect().height*3/6))
        screen.blit(to_quit, (screen.get_rect().centerx-to_quit.get_rect().width/2,screen.get_rect().height*5/6))

        #Keep Updating the Screen
        pygame.display.update()