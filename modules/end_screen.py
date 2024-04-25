'''Module for customising the end screen'''
import random
import pygame

from modules.settings import Settings
from modules.button import Button

def show(screen: pygame.Surface):

    mg_settings = Settings.End()
    screen.fill((0,0,60))

    squares = pygame.sprite.Group()
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Monospace", 70)
    title = font.render("Your Score is:", True, mg_settings.bt_text_color, mg_settings.screen_color)

    while True:
        #check_events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return "exit" 


        pos = (random.randint(0,screen.get_width()), random.randint(0,screen.get_height()))
        square = Button(screen,"The End",mg_settings.active_bt_color,mg_settings.inactive_bt_color,mg_settings.bt_text_color,50,50,pos)
        squares.add(square)

        for sprite in squares:
            sprite.update_animation()
            sprite.draw_button()

        screen.blit(title, (screen.get_rect().centerx-title.get_rect().width/2,screen.get_rect().height*1/6))

        #Keep Updating the Screen
        pygame.display.update()
        clock.tick(20)

if __name__ == "__main__":
    screen = pygame.display.set_mode((800,800))