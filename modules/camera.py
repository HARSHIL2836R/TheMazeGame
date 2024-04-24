"""Module to store the class Camera"""

from turtle import screensize, settiltangle
import pygame

#My Modules
from modules.player import Player
from modules.settings import Settings
from modules.sprites import Sprite

class Camera:
    def __init__(self, screen: pygame.Surface, map_: pygame.Surface, settings: Settings):
        self.map_ = map_
        self.settings = settings
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.camera = pygame.Rect(0,0,self.width,self.height)

    def apply(self,entity: Sprite):
        """
        Returns the coordinates for blitting the surface of Rect on the screen relative to Camera
        """
        return entity.rect.move(self.camera.topleft)
    
    def draw(self,screen: pygame.Surface,group: pygame.sprite.Group):
        """
        Blits all Sprites to screen
        """
        for sprite in group:
            screen.blit(sprite.image, self.apply(sprite))

    def update(self,target: Player)->None:
        """
        Updates the Rect of Camera according to Player
        Args:
            target: Player
        """
        boo = 1
        if boo == 1:
            #ORIGINAL WORKING
            x = int(self.screen.get_width()/2) - target.rect.centerx
            y = int(self.screen.get_height()/2) - target.rect.centery

        if boo == 0:
            #ORIGINAL WORKING
            xlimit = (self.map_.get_width()-self.screen.get_width())/2 - 3*self.settings.box_width
            ylimit = (self.map_.get_height()-self.screen.get_height())/2
            
            if (0<=target.rect.x<xlimit) or (self.screen.get_width()-xlimit<=target.rect.x<=self.screen.get_width()):
                x = self.settings.box_width
            else:
                x = int(self.screen.get_width()/2) - target.rect.centerx
            
            if(0<=target.rect.y<ylimit) or (self.screen.get_height()-ylimit<=target.rect.y<=self.screen.get_height()):
                y = 0
            else:
                y = int(self.screen.get_height()/2) - target.rect.centery

        self.camera =pygame.Rect(x,y,self.width,self.height)