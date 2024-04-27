'''Module for customising the end screen'''
import random
import sys
import pygame

#My Modules
from modules.settings import Settings
from modules.button import Button

def show(screen: pygame.Surface)->str:
    """
    Function to update the Game Screen to The End Screen and return string whether to re-run the game or exit it
    """
    mg_settings = Settings.End()
    screen.fill(mg_settings.screen_color)

    #Initialise the group to store animating sprites
    squares = pygame.sprite.Group()
    clock = pygame.time.Clock()

    ###SCREEN ELEMENTS
    font = pygame.font.SysFont("Monospace", 70)
    title = font.render("Your Score is:", True, mg_settings.bt_text_color, mg_settings.screen_color)

    #Initialising the Scoreboard object
    scoreboard = Settings.ScoreBoard()
    data = scoreboard.iterable_data()
    #Show score
    score = data[-1][1]
    font = pygame.font.Font("fonts/Arcade.ttf", 100)
    score = font.render(score, True, mg_settings.bt_text_color, mg_settings.screen_color)
    
    #Show the time_elapsed or whether the game timed out
    if data[-1][-1].strip('\n') == "0":
        font = pygame.font.SysFont("Monospace", 70)
        title_2 = font.render("Time Taken is:", True, mg_settings.bt_text_color, mg_settings.screen_color)
        font = pygame.font.Font("fonts/Arcade.ttf", 100)
        time = font.render(data[-1][-2], True, mg_settings.bt_text_color, mg_settings.screen_color)
    else:
        font = pygame.font.SysFont("Monospace", 65)
        timeout = font.render("YOUR GAME TIMED OUT!", True, mg_settings.bt_text_color, mg_settings.screen_color)
    
    font = pygame.font.SysFont("Monospace", 40)
    player_dead = font.render("WASTED", True, mg_settings.bt_text_color, mg_settings.screen_color)

    font = pygame.font.Font("fonts/led.ttf", 20)
    msg = font.render("Press ESC to exit", True, mg_settings.bt_text_color, mg_settings.screen_color)
    msg2 = font.render("Press M to return to Main Menu", True, mg_settings.bt_text_color, mg_settings.screen_color)
    ####

    while True:
        #check_events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                print("exit") 
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                pygame.quit()
                return "rerun"


        pos = (random.randint(0,screen.get_width()), random.randint(0,screen.get_height()))
        square = Button(screen,"The End",mg_settings.active_bt_color,mg_settings.inactive_bt_color,mg_settings.bt_text_color,50,50,pos)
        squares.add(square)

        for sprite in squares:
            sprite.update_animation()
            sprite.draw_button()

        ###Blit elements to screen
        screen.blit(title, (screen.get_rect().centerx-title.get_rect().width/2,screen.get_rect().height*1/6))
        screen.blit(score, (screen.get_rect().centerx-score.get_rect().width/2,screen.get_rect().height*1/3))

        if data[-1][-1].strip('\n') == "0":
            screen.blit(title_2, (screen.get_rect().centerx-title_2.get_rect().width/2,screen.get_rect().height*4/6))
            screen.blit(time, (screen.get_rect().centerx-time.get_rect().width/2,screen.get_rect().height*5/6))
        elif data[-1][-1].strip('\n') == "1":
            screen.blit(timeout, (screen.get_rect().centerx-timeout.get_rect().width/2,screen.get_rect().height*3/6))
        elif data[-1][-1].strip('\n') == "2":
            screen.blit(player_dead, (screen.get_rect().centerx-player_dead.get_rect().width/2,screen.get_rect().height*3/6))
        
        screen.blit(msg, (screen.get_rect().centerx-msg.get_rect().width/2,screen.get_rect().height*0))
        screen.blit(msg2, (screen.get_rect().centerx-msg2.get_rect().width/2,screen.get_rect().height*0.5/6))
        ###

        #Keep Updating the Screen
        pygame.display.update()
        clock.tick(20)

if __name__ == "__main__":
    screen = pygame.display.set_mode((800,800))