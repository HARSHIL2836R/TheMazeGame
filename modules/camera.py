"""Module to store the class Camera"""

import pygame
from modules.player import Player


class Camera:
    def __init__(self, screen: pygame.Surface, map_: pygame.Surface, player: Player):
        self.map_ = map_
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.camera = pygame.Rect(0,0,self.width,self.height)

    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)
    
    def draw(self,surface: pygame.Surface,group):
        for sprite in group:
            surface.blit(self.image, self.apply(sprite))

    def update(self,target):
        x = int(self.map_.get_width()/2) - target.rect.centerx
        y = int(self.map_.get_height()/2) - target.rect.centery

        self.camera = pygame.Rect(x,y,self.width,self.height)