"""Module to store the class Camera"""

import pygame

#My Modules
from modules.player import Player
from modules.settings import Settings

class Camera:
    def __init__(self, screen: pygame.Surface, map_: pygame.Surface, settings: Settings)->None:
        """
        Intialise the Camera object's attributes
        Namels, the Map/Maze over which rectangles are defined, Settings from which attributes are to be taken, Screen over which the screen will blit/display, Camera's width, height, Rect
        """
        self.map_ = map_
        self.settings = settings
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.camera = pygame.Rect(0,0,self.width,self.height)

    def apply(self,entity: pygame.sprite.Sprite)->pygame.Rect:
        """
        Returns the coordinates for blitting the surface of Rect on the screen relative to Camera
        Args:
            entity: Sprite/Rect, of whose realtive position we want to find out
        Returns:
            Rect: the coordinates used to blit the Sprites
        """
        return entity.rect.move(self.camera.topleft)
    
    def draw(self,screen: pygame.Surface,group: pygame.sprite.Group)->None:
        """
        Blits all Sprites in the group provided as parameter, to the screen
        """
        for sprite in group:
            screen.blit(sprite.image, self.apply(sprite))

    def update(self,target: Player)->None:
        """
        Updates the Rect of Camera according to Player
        Args:
            target: Player
        Returns:
            None
        """
        boo = 1
        if boo == 1:
            #ORIGINAL WORKING
            x = int(self.screen.get_width()/2) - target.rect.centerx
            y = int(self.screen.get_height()/2) - target.rect.centery

        if boo == 0:
            #NOT WORKING
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
        
        self.camera = pygame.Rect(x,y,self.width,self.height)