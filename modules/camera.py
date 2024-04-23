"""Module to store the class Camera"""

import pygame
from modules.player import Player
from modules.sprites import Sprite


class Camera:
    def __init__(self, screen: pygame.Surface, map_: pygame.Surface, player: Player):
        self.map_ = map_
        self.width = screen.get_width()/2
        self.height = screen.get_height()/2
        self.camera = pygame.Rect(0,0,self.width,self.height)

    def apply(self,entity: Sprite):
        return entity.rect.move(self.camera.topleft)
    
    def draw(self,surface: pygame.Surface,group: pygame.sprite.Group):
        for sprite in group:
            print(sprite.image)
            surface.blit(sprite.image, self.apply(sprite))

    def update(self,target: Player):
        boo = 0
        if boo == 1:
            #ORIGINAL NOT WORKING
            x = min(0, int(self.map_.get_width()/2) - target.rect.centerx)
            y = min(0, int(self.map_.get_height()/2) - target.rect.centery)

        if boo == 0:
            #ORIGINAL WORKING
            x = int(self.map_.get_width()/2) - target.rect.centerx
            y = int(self.map_.get_height()/2) - target.rect.centery

        self.camera = pygame.Rect(x, y, self.width, self.height)