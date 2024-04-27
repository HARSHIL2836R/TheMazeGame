'''Module for customising the Menu'''
import pygame

#My Modules
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
    #Scoreboard
    sorted_data = Settings.ScoreBoard().get_top_scores()
    font = pygame.font.SysFont("Monospace", 32)
    if sorted_data == None:
        pass
    elif sorted_data != None:
        data0 = font.render(str("{0:^16}".format("TimeStamp")+" -> "+"{0:^10}".format("Score")), True, mg_settings.screen_text_color, mg_settings.screen_color)
        data1 = font.render(str(sorted_data[0][0][:16]+" -> "+str(sorted_data[0][1])), True, mg_settings.screen_text_color, mg_settings.screen_color)
    elif len(sorted_data) > 1:
        data2 = font.render(str(sorted_data[1][0][:16]+" -> "+str(sorted_data[0][1])), True, mg_settings.screen_text_color, mg_settings.screen_color)
    elif len(sorted_data) > 2:
        data3 = font.render(str(sorted_data[2][0][:16]+" -> "+str(sorted_data[0][1])), True, mg_settings.screen_text_color, mg_settings.screen_color)


    def update_screen():
        mouse = pygame.mouse.get_pos()
        
        for button in {lvl1_button,lvl2_button,lvl3_button}:
            button.draw_button()
            button.update_button(mouse[0], mouse[1])

        screen.blit(title, (screen.get_rect().centerx-title.get_rect().width/2,screen.get_rect().height*0.3/6))
        if sorted_data == None:
            pass
        elif sorted_data != None:
            screen.blit(data0, (screen.get_rect().centerx-data0.get_rect().width/2,screen.get_rect().height*1/6))
            screen.blit(data1, (screen.get_rect().centerx-data1.get_rect().width/2,screen.get_rect().height*1.5/6))
        elif len(sorted_data) > 1:
            screen.blit(data2, (screen.get_rect().centerx-data2.get_rect().width/2,screen.get_rect().height*2/6))
        elif len(sorted_data) > 2:
            screen.blit(data3, (screen.get_rect().centerx-data3.get_rect().width/2,screen.get_rect().height*2.5/6))
        screen.blit(selector, (screen.get_rect().centerx-selector.get_rect().width/2,screen.get_rect().height*3.2/6))
        screen.blit(to_quit, (screen.get_rect().centerx-to_quit.get_rect().width/2,screen.get_rect().height*5/6))

        #Keep Updating the Screen
        pygame.display.update()


    while True:
        update_screen()
        
        #check_events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return "exit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for button in {lvl1_button,lvl2_button,lvl3_button}:
                    if button.rect.collidepoint(pos):
                        return button.org_msg