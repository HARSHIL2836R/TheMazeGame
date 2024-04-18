'''Module to store class of Player element'''
import pygame

class Player():

    def __init__(self, screen):
        """Initialise the player and set it starting position"""

        #Load the player image and get it's rectangular representation
        image = pygame.image.load('images/player.png')
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        print("self.rect", self.rect)
        self.screen_rect = screen.get_rect()
        print("self.screen_rect", self.screen_rect)

        #Start player at center of left edge
        self.rect.topleft = self.screen_rect.topleft
    
    def bltime(self):
        """Draws the player at it's current position"""
        self.screen.blit(self.image, self.rect)
